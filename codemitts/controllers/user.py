import cherrypy
from codemitts.authentication import getUserEmail
from codemitts.models.User import User as UserModel
from codemitts.models.Project import Project as ProjectModel
from codemitts.jinja import render_template, add_flash_message


class User():
    exposed = True

    @cherrypy.expose
    def new(self):
        data = {}
        return render_template('register.html', data)

    @cherrypy.expose
    def sign_up(self, username=None, license_agreement=None):
        if cherrypy.request.method != "POST":
            cherrypy.response.status = 405
            data = {'error_message': '405 Method not allowed'}
            return render_template('error.html', data)

        if license_agreement != 'on':
            data = {'error_message': 'Sorry män'}
            return render_template('error.html', data)

        email = getUserEmail(cherrypy.session['auth_session'])
        user = UserModel(username=username, email=email)
        user.save()

        add_flash_message("success", "You succesfully created a new account!")
        cherrypy.session.delete()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def default(self, username):
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            cherrypy.response.status = 404
            data = {'error_message': '404 User not found'}
            return render_template('error.html', data)

        projects = ProjectModel.objects(created_by=user)

        data = {'user': user, 'projects': projects}
        return render_template('user/show.html', data)
