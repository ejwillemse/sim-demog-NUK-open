# sim-demog-NUK-open

**Important note**: it has become exceedingly difficult to validate extensions to the model using completely synthetic household data. When detecting anomolies, we then have to determine whether it as a model error, or due to the input data. Development of the model has therefore shifted to a private repository using real non-public data.

sim-demog-NUK-open is an adapted and open, in that it is based on publicly available data, version of the [sim-demog python model](https://github.com/nicgeard/sim-demog), described and tested in [this article](http://jasss.soc.surrey.ac.uk/16/1/8.html).

The model has been adapted to work with Singapore demographic rates and input data. The model has been further to adapted to work with Python 3.7.

Example output of the model, in the form of a population modelled over 10 years, is available under `test/pop_output/pop_10_years.csv`. A description of the output fields can be found in `test/pop_output/pop_meta.txt`

The original model description is as follows:

  'population' directory contains python classes
  'test' contains parameters and data files (contemporary Australian population) for a simple testcase

  To run the test case, from 'test', execute 'python ../population/main.py'; a population of c10,000 will be simulated for 200 years, and data plots written to an 'output' subdirectory.

  Python libraries required (debian package names) include: python-configobj, python-numpy, python-matplotlib, python cheetah and python-imaging.
  
 The `test/` folder contains different parameter config files, input and output folders. The `population/` file contains the actual code for running the simulation. `data/` is the formal data folder with Singapore based input data, and `docs/` is the formal document folder, with documents related to the project. 

## to install and develop

after clone the repository

```sh

cd sim-demog-NUK-open
pip install -e .

```
