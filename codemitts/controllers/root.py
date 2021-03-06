import cherrypy
from codemitts.controllers.authentication import Authentication
from codemitts.controllers.project import Project
from codemitts.controllers.user import User
from codemitts.models.Project import Project as ProjectModel
from codemitts.models.User import User as UserModel
from codemitts.jinja import render_template


class Root():
    def __init__(self):
        self.authentication = Authentication()
        self.user = User()
        self.project = Project()

    @cherrypy.expose
    def index(self):
        data = {'projects': ProjectModel.objects,
                'users': UserModel.objects}
        return render_template('index.html', data)
