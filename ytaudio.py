#! /usr/bin/env python3

import os
import sys
import youtube_dl

# Pass the playlist URL and directory as arguments to the script call
playlisturl = sys.argv[1]
playlistdir = sys.argv[2]

playlistdir = playlistdir.rstrip('/')

# Create directory if not present
if not os.path.isdir(playlistdir):
    os.mkdir(playlistdir)

# Format filename for saved audio files
output = '{}/%(playlist_index)s-%(title)s.%(ext)s'.format(playlistdir)

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
        'outtmpl':output}

# Download and convert the Youtube audio
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([playlisturl])



