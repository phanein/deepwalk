import logging
from io import open
from os import path
from time import time
from itertools import izip
from multiprocessing import cpu_count
import random
from concurrent.futures import ProcessPoolExecutor

from deepwalk import graph

logger = logging.getLogger("deepwalk")

__current_graph = None

# speed up the string encoding
__vertex2str = None

def count_lines(f):
  if path.isfile(f):
    num_lines = sum(1 for line in open(f))
    return num_lines
  else:
    return 0

def _write_walks_to_disk(args):
  num_paths, path_length, alpha, rand, f = args
  G = __current_graph
  t_0 = time()
  with open(f, 'w') as fout:
    for walk in graph.build_deepwalk_corpus_iter(G=G, num_paths=num_paths, path_length=path_length,
                                                 alpha=alpha, rand=rand):
      fout.write(u"{}\n".format(u" ".join(__vertex2str[v] for v in walk)))
  logger.debug("Generated new file {}, it took {} seconds".format(f, time() - t_0))
  return f

def write_walks_to_disk(G, filebase, num_paths, path_length, alpha=0, rand=random.Random(0), num_workers=cpu_count(),
                        always_rebuild=True):
  global __current_graph
  global __vertex2str
  __current_graph = G
  __vertex2str = {v:str(v) for v in G.nodes()}
  files_list = ["{}.{}".format(filebase, str(x)) for x in xrange(num_paths)]
  expected_size = len(G)
  args_list = []
  files = []

  paths_per_worker = [len(filter(lambda x: x!= None, x)) for x in graph.grouper(num_workers, range(0, num_paths))]

  with ProcessPoolExecutor(max_workers=num_workers) as executor:
    for size, file_, ppw in izip(executor.map(count_lines, files_list), files_list, paths_per_worker):
      if always_rebuild or size != (ppw*expected_size):
        args_list.append((ppw, path_length, alpha, random.Random(rand.randint(0, 2**31)), file_))
      else:
        files.append(file_)

  with ProcessPoolExecutor(max_workers=num_workers) as executor:
    for file_ in executor.map(_write_walks_to_disk, args_list):
      files.append(file_)

  return files

def combine_files_iter(file_list):
  for file in file_list:
    with open(file, 'r') as f:
      for line in f:
        yield line.split()