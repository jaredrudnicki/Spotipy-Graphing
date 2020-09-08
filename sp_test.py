import sys
import spotipy
from matplotlib import pyplot as plt
import pandas as pd

client_secret = '6a112ea19cc04a64b18164c1218198cb'
client_id = 'ac16b07b2e97494eab56f93868924969'
redirect_uri = 'http://google.com/'

songs_list = []
artists_list = []
pop_list = []
color_list = []

"""
exit_func gathers lists about listened to songs
and places it into a dataframe and color
coded graph. Also exits the shell running
the script.
"""
def exit_func():
    d = {'name':songs_list,
         'artist':artists_list,
         'popularity':pop_list,
         'color':color_list}
    df=pd.DataFrame(d)
    print(df)
    plt.scatter(x=songs_list, y=pop_list, cmap=color_list,vmin=0,vmax=100)
    plt.show()
    exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    scope = 'user-read-currently-playing'
    token = spotipy.util.prompt_for_user_token(username, scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    if token:
        song_current = ''
        song_prev = ''
        running = True
        while running:
            #print('continue? (y/n)')
            sp = spotipy.Spotify(auth=token)
            user = sp.current_user()
            track = sp.currently_playing(market='from_token')
            song_info = track['item']

            #get the artist
            album = song_info['album']
            artists = album['artists']
            artist_links = artists[0]
            artist_name = artist_links['name']

            is_ad = track['currently_playing_type']
            track['progress_ms'] = 60000
            progress_ms = track['timestamp']
            #print(artist_name)
            #print('----------------------------------------')
            #print(is_ad)

            #get current song
            temporary = song_info['name']

            #get popularity
            popularity = song_info['popularity']
            #print('----------------------------------------')
            #print(popularity)

            #check if the song changes
            if(temporary != song_prev):
                song_current = temporary
                song_prev = temporary
                songs_list.append(song_current)
                artists_list.append(artist_name)
                pop_list.append(popularity)
                if popularity > 50:
                    color_list.append([0,255,0])
                else:
                    color_list.append([255,0,0])
                print(song_current)
                print('----------------------------------------')
                #print('would you like to stop? (y/n)')
                

                exit_input = str(input("would you like to stop?"))
                if exit_input == 'y' or exit_input == 'Y':
                    running = False
                    exit_func()
                else:
                    continue
            
          
    else:
        print("Can't get token for", username)


