import cherrypy
from codemitts.authentication import getAuthURL, getAuthSession, getUserInformation
from codemitts.models.Project import Project
from codemitts.jinja import render_template


class Root():
    def __init__(self):
        self.authentication = Authentication()

    def index(self):
        return render_template('index.html', { 'projects': Project.objects})
    index.exposed = True


class Authentication():
    exposed = True

    def oauth_login(self):
        raise cherrypy.HTTPRedirect(getAuthURL())
    oauth_login.exposed = True

    def oauth_callback(self, **params):
        # TODO Handle error messages from the API. Especially those likely to
        # occur such as "access_denied" and "redirect_uri_missmatch"
        session = getAuthSession(params['code'])
        cherrypy.session['user'] = getUserInformation(session)

        raise cherrypy.HTTPRedirect("/")
    oauth_callback.exposed = True

    def logout(self):
        cherrypy.session.delete()

        raise cherrypy.HTTPRedirect("/")
    logout.exposed = True
