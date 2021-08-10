# -*- coding: utf-8 -*-
from .__main__ import parse_args, process

__author__ = 'Bryan Perozzi'
__email__ = 'bperozzi@cs.stonybrook.edu'
__version__ = '1.0.0'


def fit(input_file, num_walks=10, dimensions=64, workers=1, output_file=None):
    """
    usage: deepwalk [-h] [--debug] [--format FORMAT] --input [INPUT] [-l LOG]
                    [--matfile-variable-name MATFILE_VARIABLE_NAME]
                    [--max-memory-data-size MAX_MEMORY_DATA_SIZE]
                    [--number-walks NUMBER_WALKS] --output OUTPUT
                    [--representation-size REPRESENTATION_SIZE] [--seed SEED]
                    [--undirected UNDIRECTED] [--vertex-freq-degree]
                    [--walk-length WALK_LENGTH] [--window-size WINDOW_SIZE]
                    [--workers WORKERS]

    deepwalk --input {adjacency_list} --number-walks 20
             --representation-size 1 --output {output_file_name}
    """
    args = [
        '--input', input_file,
        '--number-walks', str(num_walks),
        '--representation-size', str(dimensions),
        '--output', output_file,
        ]
    args = parse_args(args)
    model = process(args)
    return model
