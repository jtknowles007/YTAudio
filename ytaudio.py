#! /usr/bin/env python3

import sys
import youtube_dl

# Pass the playlist URL as an argument to the script call
playlisturl = sys.argv[1]

# Output options
options = {
        'format':'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
            }],
        'quiet': False,
        'restrictfilenames': True,
        'outtmpl':'/home/john/Music/%(playlist_index)s-%(title)s.%(ext)s'}

# Download and convert the Youtube audio
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([playlisturl])



