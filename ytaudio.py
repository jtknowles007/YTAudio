#! /usr/bin/env python3

import os
import sys
import youtube_dl

# Pass the playlist URL and directory as arguments to the script call
playlisturl = sys.argv[1]
playlistdir = sys.argv[2]

# Add / to the directory if not present
if playlistdir[-1] != '/':
    playlistdir = playlistdir+'/'

# Create directory if not present
if not os.path.isdir(playlistdir):
    os.mkdir(playlistdir)

# Output options
output = '{}%(playlist_index)s-%(title)s.%(ext)s'.format(playlistdir)
options = {
        'format':'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
            }],
        'quiet': False,
        'restrictfilenames': True,
        'outtmpl':output}

# Download and convert the Youtube audio
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([playlisturl])



