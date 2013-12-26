import cherrypy
from codemitts.authentication import getUserEmail
from codemitts.models.Project import Project as ProjectModel
from codemitts.jinja import render_template, add_flash_message


class Project():
    exposed = True

    @cherrypy.expose
    def default(self, name):
        try:
            project = ProjectModel.objects.get(name=name)
        except ProjectModel.DoesNotExist:
            cherrypy.response.status = 404
            data = {'error_message': '404 Project not found'}
            return render_template('error.html', data)

        data = {'project': project}
        return render_template('project/show.html', data)
