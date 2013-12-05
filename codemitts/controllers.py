import cherrypy
from codemitts.authentication import getAuthURL, getAuthSession, getUserEmail
from codemitts.models.Project import Project
from codemitts.models.User import User as UserModel
from codemitts.jinja import render_template


class Root():
    def __init__(self):
        self.authentication = Authentication()
        self.user = User()

    def index(self):
        data = {'projects': Project.objects,
                'users': UserModel.objects}
        return render_template('index.html', data)
    index.exposed = True


class User():
    exposed = True

    def default(self, username):
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            cherrypy.response.status = 404
            data = {'error_message': '404 User not found'}
            return render_template('error.html', data)

        data = {'user': user}
        return render_template('user.html', data)
    default.exposed = True


class Authentication():
    exposed = True

    def oauth_login(self):
        raise cherrypy.HTTPRedirect(getAuthURL())
    oauth_login.exposed = True

    def oauth_callback(self, **params):
        # TODO Handle error messages from the API. Especially those likely to
        # occur such as "access_denied" and "redirect_uri_missmatch"
        auth_session = getAuthSession(params['code'])
        email = getUserEmail(auth_session)

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            # TODO Let the user decide username
            user = UserModel(email=email, username=email)
            user.save()

        cherrypy.session['auth_session'] = auth_session
        cherrypy.session['user'] = user

        raise cherrypy.HTTPRedirect("/")
    oauth_callback.exposed = True

    def logout(self):
        cherrypy.session.delete()

        raise cherrypy.HTTPRedirect("/")
    logout.exposed = True
