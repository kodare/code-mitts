Setup
=====

Requirements
------------

*   Python 3.3
*   virtualenv - https://pypi.python.org/pypi/virtualenv
*   lessc - http://lesscss.org/
*   MongoDB - http://www.mongodb.org/

Other requirements are provided as submodules or are listed in requirements.txt.
Further details below.

You also need some OAuth2 service to be able to login right now. GitHub's
OAuth2 API is confirmed to work with Code-Mitts. Ideally it should
work with just any OAuth2 API.


Install
-------

    $ git clone http://github.com/kodare/code-mitts.git
    $ cd code-mitts
    $ virtualenv -p python3.3 ./virtualenv
    $ cp config/codemitts.ini.dist config/codemitts.ini
    Make necessary changes to config/codemitts.ini to suit your environment


Updating
--------

Whenever you get a new version you need to do the following:

    $ source virtualenv/bin/activate
    $ pip install -r requirements.txt
    $ git submodule init
    $ git submodule update
    Merge config/codemitts.ini and config/codemitts.ini.dist


Booting
-------

    $ ./run.sh


Generate test data
------------------

To generate test data for the database, run:

    $ ./loadtestdata.sh


Suggested utilities
-------------------

 * Robomongo ([http://robomongo.org/]()) - A great and simple tool for browsing MongoDB databases
