# sim-demog-NUK-open

An adapted version of the [sim-demog python model](https://github.com/nicgeard/sim-demog), described and tested in [this article](http://jasss.soc.surrey.ac.uk/16/1/8.html).

The model has been adapted to work with Singapore demographic rates and input data. The model has been further to adapted to work with Python 3.7.

The original model description is as follows:

'population' directory contains python classes
'test' contains parameters and data files (contemporary Australian population) for a simple testcase

To run the test case, from 'test', execute 'python ../population/main.py'; a population of c10,000 will be simulated for 200 years, and data plots written to an 'output' subdirectory.

Python libraries required (debian package names) include: python-configobj, python-numpy, python-matplotlib, python cheetah and python-imaging
