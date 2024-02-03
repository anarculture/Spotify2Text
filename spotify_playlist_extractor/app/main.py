import argparse
from auth import authenticate
from spotify_api import fetch_playlist_data

def main():
    parser = argparse.ArgumentParser(description='Spotify Playlist Extractor')
    parser.add_argument('playlist_id', help='Spotify Playlist ID')
    args = parser.parse_args()

    access_token = authenticate()
    if access_token:
        playlist_data = fetch_playlist_data(access_token, args.playlist_id)
        print(playlist_data)  # Placeholder for actual data handling

if __name__ == '__main__':
    main()
