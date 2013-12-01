import cherrypy
from jinja2 import Environment, PackageLoader


def render_template(filename, dictionary={}):
    views_path = 'resources/views'
    environment = Environment(loader=PackageLoader('codemitts', views_path))

    authenticated = 'user' in cherrypy.session

    environment.globals = {
        "session": cherrypy.session,
        "authenticated": authenticated
    }
    template = environment.get_template(filename)
    return template.render(dictionary)
