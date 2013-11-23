import cherrypy


class HelloWorld(object):
    def index(self):
        return "Hello World! Best wishes /Code Mitts"
    index.exposed = True

cherrypy.quickstart(HelloWorld())
