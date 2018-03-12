import requests
import configparser
from imgurpython import ImgurClient


def authenticate():
    # create new config parser and open the imgur.ini file (credentials)
    config = configparser.ConfigParser()
    config.read('imgur.ini')

    # get client credentials including: id, secret, and old refresh and access tokens
    credentials = get_credentials()

    # create a new ImgurPython client
    client = ImgurClient(credentials['client_id'], credentials['client_secret'])

    # create params for oauth2
    url = "https://api.imgur.com/oauth2/token"
    payload = {'refresh_token': credentials['refresh_token'],
               'client_id': credentials['client_id'],
               'client_secret': credentials['client_secret'],
               'grant_type': 'refresh_token'}

    # response from oauth2, which contains new refresh and access tokens
    # used imgur api instead of imgurpython since I made it before deciding to use imgurpython, and it works just fine
    response = requests.request('POST', url, data=payload)
    data = response.json()

    # set access and refresh tokens for the current client
    client.set_user_auth(data['access_token'], data['refresh_token'])

    # save new credentials to imgur.ini
    config.set('credentials', 'refresh_token', data['refresh_token'])
    config.set('credentials', 'access_token', data['access_token'])
    with open('imgur.ini', 'w') as configfile:
        config.write(configfile)

    return client


def get_credentials():
    # add all credentials into a dictionary.
    # Some parts of imgur api don't need all credentials, some do. Best to just do them all in a dict
    config = configparser.ConfigParser()
    credentials_dict = {}

    # add each credential value into a dictionary
    config.read('imgur.ini')
    credentials_dict['client_id'] = config.get('credentials', 'client_id')
    credentials_dict['client_secret'] = config.get('credentials', 'client_secret')
    credentials_dict['access_token'] = config.get('credentials', 'access_token')
    credentials_dict['refresh_token'] = config.get('credentials', 'refresh_token')

    return credentials_dict
