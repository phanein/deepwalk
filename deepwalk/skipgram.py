from collections import Counter, Mapping
from concurrent.futures import ProcessPoolExecutor
import logging
from multiprocessing import cpu_count
from six import string_types

from gensim.models import Word2Vec
from gensim.models.word2vec import Vocab

logger = logging.getLogger("deepwalk")

class Skipgram(Word2Vec):
    """A subclass to allow more customization of the Word2Vec internals."""

    def __init__(self, vocabulary_counts=None, **kwargs):

        self.vocabulary_counts = None

        kwargs["min_count"] = kwargs.get("min_count", 1)
        kwargs["workers"] = kwargs.get("workers", cpu_count())
        kwargs["size"] = kwargs.get("size", 128)
        kwargs["sentences"] = kwargs.get("sentences", None)

        if vocabulary_counts != None:
          self.vocabulary_counts = vocabulary_counts

        super(Skipgram, self).__init__(**kwargs)

    def build_vocab(self, corpus):
        """
        Build vocabulary from a sequence of sentences or from a frequency dictionary, if one was provided.
        """
        if self.vocabulary_counts != None:
          logger.debug("building vocabulary from provided frequency map")
          vocab = self.vocabulary_counts
        else:
          logger.debug("default vocabulary building")
          super(Skipgram, self).build_vocab(corpus)
          return

        # assign a unique index to each word
        self.vocab, self.index2word = {}, []

        for word, count in vocab.iteritems():
            v = Vocab()
            v.count = count
            if v.count >= self.min_count:
                v.index = len(self.vocab)
                self.index2word.append(word)
                self.vocab[word] = v

        logger.debug("total %i word types after removing those with count<%s" % (len(self.vocab), self.min_count))

        if self.hs:
            # add info about each word's Huffman encoding
            self.create_binary_tree()
        if self.negative:
            # build the table for drawing random words (for negative sampling)
            self.make_table()
        # precalculate downsampling thresholds
        self.precalc_sampling()
        self.reset_weights()