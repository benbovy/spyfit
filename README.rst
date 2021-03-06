Spyfit
======

.. image:: https://travis-ci.org/girpas-ulg/spyfit.svg?branch=master
        :target: https://travis-ci.org/girpas-ulg/spyfit
.. image:: https://coveralls.io/repos/github/girpas-ulg/spyfit/badge.svg?branch=master
        :target: https://coveralls.io/github/girpas-ulg/spyfit?branch=master
.. image:: https://landscape.io/github/girpas-ulg/spyfit/master/landscape.svg?style=flat
        :target: https://landscape.io/github/girpas-ulg/spyfit/master
        :alt: Code Health
.. image:: https://img.shields.io/pypi/v/spyfit.svg
        :target: https://pypi.python.org/pypi/spyfit
.. image:: https://readthedocs.org/projects/spyfit/badge/?version=master
        :target: http://spyfit.readthedocs.io/en/master/?badge=master
        :alt: Documentation Status

**This package is currently under heavy development:** it hasn't been released
yet (some features below are still missing but planned). API is not stable.

**Spyfit** provides a set of tools for easy handling of FTIR retrieval data and
for flexible setup and execution of retrieval processing pipelines.

Spyfit aims to provide deep integration with the libraries of the Python
scientific ecosystem and promotes the use of standard data models
such as netCDF_.

Main Features
-------------

- Uses the `Common Data Model`_ to store and handle retrieval data.
  The xarray_ package - a required dependency - implements this data model and
  provides a powerful framework for easy inspection, merging, processing and
  plotting of retrieval data.
- Supports various formats including:
    - netCDF_ (read/write)
    - SFIT4_ ascii output files (read-only) and input files (read, write support
      for the most used input files)
    - GEOMS_ compliant HDF4 format (read/write)
    - Easy export to various formats supported by xarray_ and pandas_
      (e.g., hdf5, csv, excel, SQL-databases...)
- Tries to use readable, "pythonic" names for parameters and variables.
- Calculation of retrieval error budgets (SFIT4).
- Defines a basic, class-based system for flexible setup and execution
  of retrieval pipelines (possibly including the execution of third-party
  softwares like SFIT4).

.. _SFIT4: https://wiki.ucar.edu/display/sfit4/Infrared+Working+Group+Retrieval+Code,+SFIT
.. _Common Data Model: http://www.unidata.ucar.edu/software/thredds/current/netcdf-java/CDM
.. _netCDF: http://www.unidata.ucar.edu/software/netcdf
.. _xarray: http://xarray.pydata.org
.. _pandas: http://pandas.pydata.org/
.. _GEOMS: http://avdc.gsfc.nasa.gov/index.php?site=1178067684

Documentation
-------------

The official documentation is hosted on ReadTheDocs: https://spyfit.readthedocs.org.

Report Issues
-------------

Use the Github issue tracker: https://github.com/girpas-ulg/spyfit/issues

License
-------

Copyright (C) Benoit Bovy, GIRPAS (Ulg) 2015.

Licensed under the GNU General Public License (GPLv3_). See LICENSE.

.. _GPLv3: http://www.gnu.org/licenses/gpl-3.0.fr.html
