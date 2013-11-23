import cherrypy
from jinja2 import Environment, PackageLoader

environment = Environment(loader=PackageLoader('codemitts', 'templates'))


class Root(object):
    @cherrypy.expose
    def index(self):
        template = environment.get_template('index.html')
        return template.render()

cherrypy.quickstart(Root())
