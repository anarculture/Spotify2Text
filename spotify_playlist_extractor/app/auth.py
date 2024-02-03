import webbrowser
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

def authenticate():
    # Step 1: User Authorization
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPES,
    }
    webbrowser.open(AUTH_URL + '?' + '&'.join([f'{key}={value}' for key, value in params.items()]))

    # Step 2: Local Server to catch the redirect
    class SpotifyAuthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200, 'OK')
            self.end_headers()
            self.server.path = self.path

    server = HTTPServer(('localhost', 8888), SpotifyAuthHandler)
    server.handle_request()
    authorization_response = server.path
    code = authorization_response.split('code=')[1]

    # Step 3: Requesting Access Token
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    response = requests.post(TOKEN_URL, data=payload).json()
    return response.get('access_token')

