from cherrypy import quickstart
from codemitts.controllers import Root
from codemitts.assets import compileLess
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy_config = {
    '/': {
        'tools.staticdir.root': current_dir
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': "resources/static"
    }
}
compileLess()
quickstart(Root(), "", cherrypy_config)
