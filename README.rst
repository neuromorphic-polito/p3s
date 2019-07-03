P3S: the PoliTO SpiNNaker Software Stack
----------------------------------------

This repository contains all the software requirements needed to use the SpiNNaker architecture with the MPI programming model.

The software stack is composed of three layers (MCM, ACP, MPI) in order to provide features with different abstraction levels.

Installation
------------

Requirements:

* git
* python 2.7.x
* virtualenv
* gcc
* cmake
* arm-none-eabi-gcc
* Perl 5

1. In the p3s folder, call the download, setup and compilation script:

::

	% python install.py

2. Activate the virtual environment:

::

	% source activate.sh

Usage instructions
------------------

Activate the virtual environment before compiling or running any MPI applications for SpiNNaker.

In the p3s folder:

::

	% source activate.sh

Authorship and copyright
------------------------

P3S is being developed by `Francesco Barchi <mailto:francesco.barchi@polito.it>`__ and `Evelina Forno <mailto:evelina.forno@polito.it>`__.

+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Please respect the license of the software**                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| .. image:: https://user-images.githubusercontent.com/7613428/60581999-4168a180-9d88-11e9-87e3-ce5e127b84a1.png   | p3s is free and open source software, so you can use it for any purpose, free of charge.                           |
|    :alt: Respect the license                                                                                     | However, certain conditions apply when you (re-)distribute and/or modify p3s; please respect the                   |
|    :target: https://github.com/neuromorphic-polito/p3s/blob/master/LICENSE.rst                                   | `license <https://github.com/neuromorphic-polito/p3s/blob/master/LICENSE.rst>`__.                                  |
|    :width: 76px                                                                                                  |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

*icons on this page by Austin Andrews / https://github.com/Templarian/WindowsIcons*
