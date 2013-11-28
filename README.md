Setup
=====

Requirements
------------

*   Python 3.3
*   virtualenv - https://pypi.python.org/pypi/virtualenv
*   lessc - http://lesscss.org/

Other requirements are provided as submodules or are listed in requirements.txt.
Further details below.


Install
-------

    $ git clone http://github.com/kodare/code-mitts.git
    $ cd code-mitts
    $ virtualenv -p python3.3 ./virtualenv


Get all dependencies
--------------------

Whenever you get a new version you need to do the following:

    $ source virtualenv/bin/activate
    $ pip install -r requirements.txt
    $ git submodule init
    $ git submodule update


Booting
-------

    $ ./run.sh
