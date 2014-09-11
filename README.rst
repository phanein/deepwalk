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
    
    3. ``--format mat`` for a Matlab MAT file containing an adjacency matrix
        (note, you must also specify the variable name of the adjacency matrix ``--matfile-variable-name``)

**--output**: *output_filename*

    The output representations in skipgram format - first line is header, all other lines are node-id and *d* dimensional representation::

        34 64
        1 0.016579 -0.033659 0.342167 -0.046998 ...
        2 -0.007003 0.265891 -0.351422 0.043923 ...
        ...

**Full Command List**
    The full list of command line options is available with ``$deepwalk --help``

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
