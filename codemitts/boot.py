import os
from cherrypy import quickstart
from codemitts.models import database_connect
from codemitts.controllers import Root
from codemitts.assets import compileLess

# Connect to the database
database_connect('codemitts')

current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy_config = {
    '/': {
        'tools.staticdir.root': current_dir,
        'tools.sessions.on': True
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': "resources/static"
    }
}
compileLess()
quickstart(Root(), "", cherrypy_config)
