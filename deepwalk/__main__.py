#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
from io import open
from argparse import ArgumentParser, FileType, ArgumentDefaultsHelpFormatter
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import logging

from deepwalk import graph
from gensim.models import Word2Vec

from six import text_type as unicode
from six import iteritems

logger = logging.getLogger(__name__)
LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s: %(lineno)s %(message)s"

def debug(type_, value, tb):
  if hasattr(sys, 'ps1') or not sys.stderr.isatty():
    sys.__excepthook__(type_, value, tb)
  else:
    import traceback
    import pdb
    traceback.print_exception(type_, value, tb)
    print(u"\n")
    pdb.pm()

def process(args):

  G = graph.load_adjacencylist(args.input, undirected=True)
  
  print("Number of nodes: {}".format(len(G.nodes())))

  walks = graph.build_deepwalk_corpus(G, num_paths=args.number_walks, path_length=args.walk_length, alpha=0, rand=random.Random(args.seed))

  print("Number of walks: {}".format(len(walks)))

  model = Word2Vec(walks, size=args.representation_size, window=args.window_size, min_count=0, workers=args.workers)

  model.save_word2vec_format(args.output)

def main():
  parser = ArgumentParser("deepwalk",
                          formatter_class=ArgumentDefaultsHelpFormatter,
                          conflict_handler='resolve')
  parser.add_argument('--format', default='text', help='File format')
  parser.add_argument('--workers', default=1, type=int,
                      help='Number of parallel processes.')
  parser.add_argument('--input', nargs='?',
                      default=sys.stdin)
  parser.add_argument('--output')
  parser.add_argument("-l", "--log", dest="log", help="log verbosity level",
                      default="INFO")
  parser.add_argument("--debug", dest="debug", action='store_true', default=False,
                      help="drop a debugger if an exception is raised.")
  parser.add_argument('--walk-length', default=40, type=int, help='Length of the random walk started at each node')
  parser.add_argument('--number-walks', default=10, type=int, help='Number of random walks to start at each node')
  parser.add_argument('--representation-size', default=64, type=int, help='Number of latent dimensions to learn for each node.')
  parser.add_argument('--window-size', default=5, type=int, help='Window size of skipgram model.')
  parser.add_argument('--seed', default=0, type=int, help='Seed for random walk generator.')

  args = parser.parse_args()
  numeric_level = getattr(logging, args.log.upper(), None)
  logging.basicConfig(format=LOGFORMAT)
  logger.setLevel(numeric_level)

  if args.debug:
   sys.excepthook = debug 

  process(args)

if __name__ == "__main__":
  sys.exit(main())
