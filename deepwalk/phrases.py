import logging

from gensim.models.phrases import Phrases, Phraser

logger = logging.getLogger("deepwalk")

def build_ngram(walks, ngram, min_count=5, threshold=10.0,
                max_vocab_size=40000000, delimiter=b'_', scoring='default'):
    """
    Compose n-gram on the fly given tunable parameters, work for both in-memory or out-of-core computations.

    Required Parameters
    - walks: iterable list of str (iterable list of list of string, or deepwalk.walks.WalksCorpus object)
            Input random walk sequences. Can be either 'List of list of tokens'(in-memory) or 'deepwalk.walks.WalksCorpus' object(out-of-core)
    - ngram: int
            Specify the n of n-gram, e.g.: ngram=2 to compose bigrams.

    Optional Parameters
      Referece to gensim.models.phrases.Phrases

    Return
    - iterable list of str (iterable list of list of string, or deepwalk.walks.WalksCorpus object)
    """

    if ngram<2:
        logger.warning("ngram must >=2! Skip building ngram.")
        return walks

    for n in range(2,ngram+1):
        logger.info("Composing "+str(n)+"-grams...")
        ngram_phrases = Phrases(walks, min_count=min_count, threshold=threshold, max_vocab_size=max_vocab_size,
                                delimiter=delimiter, scoring=scoring)
        ngram_phraser = Phraser(ngram_phrases)
        walks = ngram_phraser[walks]

    return walks
