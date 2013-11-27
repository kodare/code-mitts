Setup
=====

Requirements
------------

*   Python 3.3
*   virtualenv - https://pypi.python.org/pypi/virtualenv

Other requirements are listed in requirements.txt and should be installed using
pip in the environment provided by virtualenv.


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
