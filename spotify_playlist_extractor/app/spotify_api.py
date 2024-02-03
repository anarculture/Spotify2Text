import requests
from config import CLIENT_ID, CLIENT_SECRET

def fetch_playlist_data(access_token, playlist_id):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=headers)
    return response.json()  # Placeholder for actual processing
