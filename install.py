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
# install.py: downloads and installs all the required dependencies for
#             running programs using the MPI programming model on SpiNNaker
# ==========================================================================

from __future__ import print_function

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import os
import subprocess


class Install:
    pyvenv = ".pyvenv"

    def __init__(self, run):
        self.run = run

        self.config = dict()
        with open("config.txt", "r") as fp:
            text = fp.read()

        phases = text.split('#')
#        self.url = phases[0].strip()

        self._phase1 = list()
        for line in phases[1].strip().split('\n'):
            line_list = line.strip().split(',')
            assert len(line_list) == 3
            line_list[2] = line_list[2] if line_list[2] != '' else line_list[0]
            self._phase1.append(line_list)
        # print("Phase1", self._phase1)

        self._phase2 = list()
        for line in phases[2].strip().split('\n'):
            self._phase2.append(line.strip())
        # print("Phase2", self._phase2)

        self._phase3 = list()
        for line in phases[3].strip().split('\n'):
            line_list = line.strip().split(',')
            assert len(line_list) == 2
            line_list[1] = True if line_list[1] == '*' else False
            self._phase3.append(line_list)
        # print("Phase3", self._phase3)

    def download(self):
        temp = "_temp_download.sh"
        with open(temp, "w") as fp:
            for repo_url, repo_commit, repo_dir in self._phase1:
                if repo_dir is None:
                    repo_dir = repo_url
                print("rm -rf {}".format(repo_dir),
                      file=fp)
#                print("git clone {url}/{repo_url} {repo_dir}".format(
#                    url=self.url, repo_url=repo_url, repo_dir=repo_dir), file=fp)
                print("git clone {repo_url} {repo_dir}".format(
                    repo_url=repo_url, repo_dir=repo_dir), file=fp)
                print("cd {}; git -c advice.detachedHead=false checkout {}; cd ..".format(repo_dir, repo_commit),
                      file=fp)

        if self.run:
            subprocess.call(["/bin/bash", temp])
            subprocess.call(["rm", "-f", temp])

    def python_install(self):
        temp = "_temp_python_install.sh"
        with open(temp, "w") as fp:
            print("rm -rf ./{}".format(Install.pyvenv),
                  file=fp)
            print("virtualenv --python=python2.7 ./{}".format(Install.pyvenv),
                  file=fp)
            print("source ./{}/bin/activate".format(Install.pyvenv),
                  file=fp)
            print("pip install -r requirements.txt",
                  file=fp)
            for repo_dir in self._phase2:
                print("cd {}; python setup.py develop; cd -".format(repo_dir),
                      file=fp)

        if self.run:
            subprocess.call(["/bin/bash", temp])
            subprocess.call(["rm", "-f", temp])

    def compile(self):
        temp = "_temp_compile.sh"
        with open(temp, "w") as fp:
            #print("source ./spinnaker_tools/setup",
            #      file=fp)

            selfpath = os.getcwd()
            
            s = ""
            s += "export SPINN_DIRS={}\n".format(
                os.path.join(selfpath, "m3s", "spinnaker_tools"))
            s += "export SPINN_PATH=$SPINN_DIRS/tools/boot\n"
            s += "export NEURAL_MODELLING_DIRS={}\n".format(
                os.path.join(selfpath, "m3s", "spynnaker", "neural_modelling"))
            s += "export PATH=$SPINN_DIRS/tools:$PATH\n"
            s += "export PERL5LIB=$SPINN_DIRS/tools:$PERL5LIB\n"
            s += "chmod u+x $SPINN_DIRS/tools/*\n"
            print(s, file=fp)
            
            for repo_dir, install in self._phase3:
                print("cd {}; make; cd -".format(repo_dir),
                      file=fp)
                if install:
                    print("cd {}; make install; cd -".format(repo_dir),
                          file=fp)

        if self.run:
            subprocess.call(["/bin/bash", temp])
            subprocess.call(["rm", "-f", temp])


def main():
    i = Install(True)
    i.download()
    i.python_install()
    i.compile()


if __name__ == "__main__":
    main()

