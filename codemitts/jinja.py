import copy
import cherrypy
from jinja2 import Environment, PackageLoader


def render_template(filename, dictionary={}):
    views_path = 'resources/views'
    environment = Environment(loader=PackageLoader('codemitts', views_path))

    authenticated = 'user' in cherrypy.session

    flash_messages = get_flash_messages()
    clear_flash_messages()

    environment.globals = {
        "session": cherrypy.session,
        "authenticated": authenticated,
        "flash_messages": flash_messages
    }
    template = environment.get_template(filename)
    return template.render(dictionary)


def add_flash_message(type, content):
    message = {"type": type, "content": content}

    count = len(cherrypy.session['flash_messages'].keys())
    if 'flash_messages' in cherrypy.session:
        count = len(cherrypy.session['flash_messages'].keys())
    else:
        count = 0
        cherrypy.session['flash_messages'] = {}

    cherrypy.session['flash_messages'][count] = {"type": type, "content": content}


def get_flash_messages():
    if 'flash_messages' in cherrypy.session.keys():
        return copy.deepcopy(cherrypy.session['flash_messages'])
    return {}


def clear_flash_messages():
    cherrypy.session['flash_messages'] = {}
