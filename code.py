import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

'''clientid and client secret vary so each user has to input their own for that spotify web developer page has to be used
also the redirect uri is also dependent on the user it is basically the url to be directed to
of your website but localhost location can be used
i used http://localhost:8888/callback'''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                               client_secret='your_client_secret',
                                               redirect_uri='your_redirect_uri',
                                               scope=['user-library-read']))

user_playlists = sp.current_user_playlists()


liked_songs_playlist = next((playlist for playlist in user_playlists['items'] if playlist['name'] == 'Coke studio'), None)


if liked_songs_playlist:
    liked_songs_tracks = sp.playlist_tracks(liked_songs_playlist['id'])
    print(f"Number of Songs in playlist: {liked_songs_tracks['total']}")


    csv_filename = 'liked_songs.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Track Name', 'Artist']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()


        for track in liked_songs_tracks['items']:
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            csv_writer.writerow({'Track Name': track_name, 'Artist': artist_name})
            print(f"{track_name} by {artist_name}")

    print(f"songs exported to {csv_filename}")
else:
    print("Playlist not found.")
