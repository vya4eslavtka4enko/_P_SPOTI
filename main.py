import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


date_for_travel = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD:')
# "div lrv-u-position-relative a-show-on-hover-parent a-chart-datepicker-opener"
URL = 'https://www.billboard.com/charts/hot-100/2000-06-03/'
response = requests.get('https://www.billboard.com/charts/hot-100/' + date_for_travel)
web_site = response.text
# print(web_site)
soup = BeautifulSoup(web_site,'html.parser')
song_name_span = soup.select('li ul li h3')
song_names = [song.getText().strip() for song in song_name_span]
# print(f'{song_names}+\n')

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='',
        client_secret='
        show_dialog=True,
        cache_path="token.txt",
        username='',
    ))

print(spotify)