from pytube import Playlist
from itertools import islice

import os
import subprocess
import threading

URL = 'https://youtube.com/playlist?list=PLF4MN-GyjkoumWXOJlOp7JBcg6sLIWCyG&si=dt15AZyr9YoA6Cdc'
WAV = 'wav\\'

def yt_to_wav(video):
    title = video.title.split('|')[0].rstrip()
    
    src = WAV + title + '.mp3'
    dst = WAV + title + '.wav'
    
    mp3 = video.streams.filter(only_audio=True).first()
    mp3.download(filename=src)
    
    try:
        subprocess.call(['ffmpeg', '-y', '-i', src, dst], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        print('[ Y ] ' + title)
    except Exception as e:
        print('[ N ] ' + title)
        print(e)

    os.remove(src)

threads = []

for video in Playlist(URL).videos:
    thread = threading.Thread(target=yt_to_wav, args=(video,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
