===============================
DeepWalk
===============================

Usage
-----
$deepwalk --help

input:  adjacency list

    1 2 3 4 5 6 7 8 9 11 12 13 14 18 20 22 32

    2 1 3 4 8 14 18 20 22 31

    3 1 2 4 8 9 10 14 28 29 33

    ...

output: representations in skipgram format - first line is header, all other lines are node-id and representation

    34 64

    1 0.016579 -0.033659 0.342167 -0.046998 ...

    2 -0.007003 0.265891 -0.351422 0.043923 ...

    ...


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
    @inproceedings{2014-perozzi-deepwalk,

    author    = {Bryan Perozzi and Rami Al-Rfou and Steven Skiena},

    title     = {DeepWalk: Online Learning of Social Representations},

    booktitle = {Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},

    series = {KDD '14},

    year = {2014},

    month = {August},

    location = {New York, NY, USA},

    publisher = {ACM},
    
    address = {New York, NY, USA},
    
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