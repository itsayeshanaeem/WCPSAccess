# WCPSAccess
Accessing Array Databases With Python via use of WCPS query language

Copyright 2003 - 2016 Peter Baumann / rasdaman GmbH.
* Multidimensional Discrete Data has become extensively utilised in various areas which are related to earth,space and life sciences. 
* Rasdaman raster data manager enables the storage of multi dimensional array data, and provides an interface to access geo spatial data -> provides services WCS, WCPS, WPS.
* WCPS is web query language allowing retrieval and processing of multi dimensional coverages 
* As there are a growing number of python users there should be a way to easily implement these queries without having any deep knowledge of wcps via an easy interface. 
* My project focuses on creating that interface that allows to extend WCPS query creation via use of Python.

Queries Type Supported
========================
* Covergae Condensor
* Coverage Subsetting
* Coverage Filtering
* Induced Operation
* Multi Band 
* Coverage Constrcutor

To run
========================
::

    $ python3 main.py
    
After this interact according to query type
========================
::
    
      $ enter query type
      $ coverage name
      $ encoding type
      $ other operations

Contributors
============
* Ayesha Naeem

Thanks also to
==============
* Peter Baumann
