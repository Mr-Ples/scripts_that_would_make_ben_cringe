import json
import os
import time
import spotipy
import random
import requests
import json

from dotenv import set_key
from lib import env
from inputimeout import inputimeout, TimeoutOccurred

random.seed(time.time())
sp = None

USER_ID = "k3e1zpksc5stgc7l3hlqx2dd6"
ADDED_TRACKS = os.path.join(env.REPO_PATH, 'spotify', 'added_tracks.txt')
SAVED_TRACKS = os.path.join(env.REPO_PATH, 'spotify', 'saved_tracks.txt')

def get_all_saved_tracks():
    global sp

    offset = 0
    limit = 50  # Maximum limit per request is 50

    with open(SAVED_TRACKS, 'r') as f:
        all_tracks = [track.strip() for track in f.readlines()]
    new_tracks = []
    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        tracks = [item['track']['id'] for item in results['items'] if item['track']['id'].strip() not in all_tracks]
        new_tracks.extend(tracks)
        if len(tracks) < 50:
            break

        offset += limit
    # Shuffle the songs
    random.shuffle(new_tracks)
    with open(SAVED_TRACKS, 'a+') as f:
        f.write('\n'.join(new_tracks))
    with open(SAVED_TRACKS, 'r') as f:
        all_tracks = [track.strip() for track in f.readlines()]
    return all_tracks


def update_uncategorized_playlist():
    global sp

    try:
        playlist = sp.playlist(os.environ["SPOTIFY_UNCATEGORIZED_PLAYLIST_ID"])
        playlist['id']
    except:
        playlist = sp.user_playlist_create(USER_ID, 'Uncategorized')
        print("NEW ID:", playlist['id'])
        set_key(env.ENV_PATH, playlist['id'], os.environ["SPOTIFY_UNCATEGORIZED_PLAYLIST_ID"])

    with open(ADDED_TRACKS, 'r') as f:
        added_tracks = [track.strip() for track in f.readlines()]
    liked_songs = list(set([track for track in get_all_saved_tracks() if track.strip() not in added_tracks]))
    chunks = [liked_songs[i:i + 100] for i in range(0, len(liked_songs) + 100, 100)]

    for chunk in chunks:
        print(str(chunks.index(chunk)) + "/" + str(len(chunks)))
        # Add the liked songs to the new playlist
        sp.playlist_add_items(playlist['id'], chunk)
        with open(ADDED_TRACKS, 'a+') as f:
            f.write('\n'.join(chunk))
        time.sleep(0.2)


def play_song(song_id):
    uri = f'qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "spotify:track:{song_id}"'
    os.system(uri)


def refresh_token():
    # Fetch the environment variables containing the client ID, client secret, and refresh token
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    refresh_token = os.environ['SPOTIFY_REFRESH_TOKEN']

    # Construct the request URL and payload for refreshing the access token
    url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Send the POST request to refresh the access token
    response = requests.post(url, data=payload)

    # Extract the new access token from the response
    access_token = response.json()['access_token']
    set_key(env.ENV_PATH, access_token, os.environ["SPOTIFY_ACCESS_TOKEN"])


def play_uncategorized():
    # with open(ADDED_TRACKS, 'r') as f:
    #     added_tracks = [track.strip() for track in f.readlines()]
    # print(ADDED_TRACKS)
    uncat_tracks = [item['track']['id'] for item in sp.playlist_items(os.environ["SPOTIFY_UNCATEGORIZED_PLAYLIST_ID"])['items']]
    random.shuffle(uncat_tracks)
    for track in uncat_tracks:
        print(track)
        play_song(track)
        while True:
            try:
                currently_playing = sp.currently_playing()['item']['id']
                break
            except:
                time.sleep(1)

        while track != currently_playing:
            print("Waiting for track to start")
            time.sleep(3)
            currently_playing = sp.currently_playing()['item']['id']

        while track == currently_playing:
            try:
                current_playlists = sp.current_user_playlists()
                playlists = {index + 1: {'id': item['id'], 'name': item['name']} for index, item in enumerate(current_playlists['items'])}
                print(json.dumps(playlists, indent=4))
                user_input = inputimeout(prompt='Pick a playlist: \n', timeout=5)
                if 's' in user_input:
                    break
                if user_input.isdecimal():
                    playlist_data = playlists[int(user_input)]
                    sp.playlist_add_items(playlist_data['id'], [track])
                    sp.playlist_remove_all_occurrences_of_items(os.environ["SPOTIFY_UNCATEGORIZED_PLAYLIST_ID"], [track])
                else:
                    new_playlist = sp.user_playlist_create(USER_ID, user_input)
                    sp.playlist_add_items(new_playlist['id'], [track])
                    sp.playlist_remove_all_occurrences_of_items(os.environ["SPOTIFY_UNCATEGORIZED_PLAYLIST_ID"], [track])
            except TimeoutOccurred:
                continue

            currently_playing = sp.currently_playing()['item']['id']


def main():
    global sp

    # Authenticate with Spotify
    sp = spotipy.Spotify(auth=os.environ['SPOTIFY_ACCESS_TOKEN'])
    # update_uncategorized_playlist() sd sd
    play_uncategorized()

    # # Start playing the songs
    # sp.add_to_queue(uri='5aQwKSYRyV1H44GsH3slJk')
    #
    # # Add user input functionality
    # while True:
    #     print("Enter the name of the playlist where you want to add the song:")
    #     playlist_name = input()
    #
    #     # Get the user's playlists
    #     playlists = sp.current_user_playlists()
    #     playlist_names = [pl['name'] for pl in playlists['items']]
    #
    #     if playlist_name in playlist_names:
    #         # Add the song to the existing playlist
    #         playlist_id = [pl['id'] for pl in playlists['items'] if pl['name'] == playlist_name][0]
    #         sp.playlist_add_items(playlist_id, [current_song])
    #     else:
    #         # Create a new playlist and add the song
    #         new_playlist = sp.user_playlist_create(user_id, playlist_name)
    #         sp.playlist_add_items(new_playlist['id'], [current_song])


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except Exception as err:
            if "access token expired" in str(err).lower():
                if refresh_token():
                    continue
            raise