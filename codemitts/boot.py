import os
import cherrypy
from codemitts.assets import compileLess, compileJavascript
from codemitts.models import database_connect
from codemitts.controllers.root import Root
from codemitts.config import config as codemitts_config


database_connect('codemitts')
compileLess()
compileJavascript()

config = {
    '/': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.sessions.on': True
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': "resources/static"
    }
}

cherrypy.tree.mount(root=Root(), config=config)

cherrypy.config.update({
    'server.socket_host': codemitts_config['webserver']['host'],
    'server.socket_port': int(codemitts_config['webserver']['port'])
})

cherrypy.engine.start()
cherrypy.engine.block()
