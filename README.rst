===============================
DeepWalk
===============================

DeepWalk uses short random walks to learn representations for vertices in graphs.

Usage
-----

**Example Usage**
    ``$deepwalk --input example_graphs/karate.adjlist --output karate.embeddings``

**--input**:  *input_filename*

    1. ``--format adjlist`` for an adjacency list, e.g::

        1 2 3 4 5 6 7 8 9 11 12 13 14 18 20 22 32
        2 1 3 4 8 14 18 20 22 31
        3 1 2 4 8 9 10 14 28 29 33
        ...
    
    2. ``--format edgelist`` for an edge list, e.g::
    
        1 2
        1 3
        1 4
        ...
    
    3. ``--format mat`` for a Matlab .mat file containing an adjacency matrix
        (note, you must also specify the variable name of the adjacency matrix ``--matfile-variable-name``)

**--output**: *output_filename*

    The output representations in skipgram format - first line is header, all other lines are node-id and *d* dimensional representation::

        34 64
        1 0.016579 -0.033659 0.342167 -0.046998 ...
        2 -0.007003 0.265891 -0.351422 0.043923 ...
        ...

**Full Command List**
    The full list of command line options is available with ``$deepwalk --help``

Evaluation
----------
Here, we will show how to evaluate DeepWalk on the *BlogCatalog* dataset used in the DeepWalk paper.
First, we run the following command to produce its DeepWalk embeddings::

    deepwalk --format mat --input example_graphs/blogcatalog.mat
    --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10
    --workers 1 --output example_graphs/blogcatalog.embeddings

The parameters specified here are the same as in the paper.
If you are using a multi-core machine, try to set ``--workers`` to a larger number for faster training.
On a single machine with 24 Xeon E5-2620 @ 2.00GHz CPUs, this command takes about 20 minutes to finish (``--workers`` is set to 20).
Then, we evaluate the learned embeddings on a multi-label node classification task with ``example_graphs/scoring.py``::

    python example_graphs/scoring.py --emb example_graphs/blogcatalog.embeddings
    --network example_graphs/blogcatalog.mat
    --num-shuffle 10 --all

This command finishes in 8 minutes on the same machine. For faster evaluation, you can set ``--num-shuffle`` to a smaller number, but expect more fluctuation in performance. The micro F1 and macro F1 scores we get with different ratio of labeled nodes are as follows:

+-----------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| % Labeled Nodes | 10%   | 20%   | 30%   | 40%   | 50%   | 60%   | 70%   | 80%   | 90%   |
+=================+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| *Micro-F1 (%)*  | 35.86 | 38.51 | 39.96 | 40.76 | 41.51 | 41.85 | 42.27 | 42.35 | 42.40 |
+-----------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| *Macro-F1 (%)*  | 21.08 | 23.98 | 25.71 | 26.73 | 27.68 | 28.28 | 28.88 | 28.70 | 28.21 |
+-----------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+

**Note that the current version of DeepWalk is based on a newer version of gensim, which may have a different implementation of the word2vec model. To completely reproduce the results in our paper, you will probably have to install an older version of gensim(version 0.10.2).**

Requirements
------------
* numpy
* scipy

(may have to be independently installed) 



Installation
------------
#. cd deepwalk
#. pip install -r requirements.txt 
#. python setup.py install


Citing
------
If you find DeepWalk useful in your research, we ask that you cite the following paper::

    @inproceedings{Perozzi:2014:DOL:2623330.2623732,
     author = {Perozzi, Bryan and Al-Rfou, Rami and Skiena, Steven},
     title = {DeepWalk: Online Learning of Social Representations},
     booktitle = {Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
     series = {KDD '14},
     year = {2014},
     isbn = {978-1-4503-2956-9},
     location = {New York, New York, USA},
     pages = {701--710},
     numpages = {10},
     url = {http://doi.acm.org/10.1145/2623330.2623732},
     doi = {10.1145/2623330.2623732},
     acmid = {2623732},
     publisher = {ACM},
     address = {New York, NY, USA},
     keywords = {deep learning, latent representations, learning with partial labels, network classification, online learning, social networks},
    } 

Misc
----

DeepWalk - Online learning of social representations.

* Free software: GPLv3 license
* Documentation: http://deepwalk.readthedocs.org.



.. image:: https://badge.fury.io/py/deepwalk.png
    :target: http://badge.fury.io/py/deepwalk

.. image:: https://travis-ci.org/phanein/deepwalk.png?branch=master
        :target: https://travis-ci.org/phanein/deepwalk

.. image:: https://pypip.in/d/deepwalk/badge.png
        :target: https://pypi.python.org/pypi/deepwalk
