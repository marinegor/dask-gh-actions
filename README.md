# dask-gh-actions
A toy repository that tests ability to run tests of dask with pytest

# Notebook

`test.ipynb` notebook contains two things:

 - a toy example of RMSD/RMSF calculations for "trajectory". The calculations get ~3x speedup with 4 workers, which is good!
 - a playground for working with process PIDs, which are later used with `pytest` to make sure things are acutally working with dask setup


