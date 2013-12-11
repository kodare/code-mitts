import cherrypy
from codemitts.authentication import getAuthURL, getAuthSession, getUserEmail
from codemitts.models.User import User as UserModel
from codemitts.jinja import render_template, add_flash_message


class Authentication():
    exposed = True

    @cherrypy.expose
    def oauth_sign_in(self):
        raise cherrypy.HTTPRedirect(getAuthURL())

    @cherrypy.expose
    def oauth_callback(self, **params):
        # TODO Handle error messages from the API. Especially those likely to
        # occur such as "access_denied" and "redirect_uri_missmatch"

        try:
            auth_session = getAuthSession(params['code'])
        except KeyError:
            # TODO Determine the best status code for this scenario
            cherrypy.response.status = 409
            data = {'error_message': '409 OAuth2 service disliked the request'}
            return render_template('error.html', data)

        email = getUserEmail(auth_session)
        cherrypy.session['auth_session'] = auth_session

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            add_flash_message("info", "You don't got an account yet!")
            raise cherrypy.HTTPRedirect("/user/new")

        add_flash_message("success", "You successfully signed in!")
        cherrypy.session['user'] = user

        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def sign_out(self):
        cherrypy.session.delete()

        raise cherrypy.HTTPRedirect("/")
