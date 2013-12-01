from rauth import OAuth2Service
from config import config

oauth2_config = config['oauth2']

service = OAuth2Service(
    name=oauth2_config['name'],
    client_id=oauth2_config['client_id'],
    client_secret=oauth2_config['client_secret'],
    authorize_url=oauth2_config['authorize_url'],
    access_token_url=oauth2_config['access_token_url'],
    base_url=oauth2_config['base_url'])


def getAuthURL():
    params = {'redirect_uri': oauth2_config['callback_url'], 'response_type': 'code'}
    return service.get_authorize_url(**params)


def getAuthSession(code):
    return service.get_auth_session(data={'code': code})


def getUserInformation(auth_session):
    # TODO This may not be the correct url for all APIs obviously - but it
    # works with GitHub. We need to figure out the correct url for the API
    # being used. Somehow.
    api_url = oauth2_config['base_url'] + 'user'
    result = auth_session.get(api_url, params={'format': 'json'})
    return result.json()
