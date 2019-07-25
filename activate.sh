#!/usr/bin/env bash

# ==========================================================================
#                                  P3S
# ==========================================================================
# This file is part of P3S.
#
# P3S is Free Software: you can redistribute it and/or modify it
# under the terms found in the LICENSE[.md|.rst] file distributed
# together with this file.
#
# P3S is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# ==========================================================================
# Author: Francesco Barchi <francesco.barchi@polito.it>
# Author: Evelina Forno <evelina.forno@polito.it>
# ==========================================================================
# activate.sh: shell script to activate the virtual environment for running
#			   MPI-enabled programs on SpiNNaker
# ==========================================================================

source ./.pyvenv/bin/activate
cd ./spinnaker_tools
source ./setup
cd -
