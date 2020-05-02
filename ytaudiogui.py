#! /usr/bin/env python3

import os
import sys
import PySimpleGUI as sg
import youtube_dl


if len(sys.argv) ==1:
    event, values = sg.Window('YTaudio',
            [[sg.Text('Playlist URL')],
            [sg.In()],
            [sg.Text('Directory Name')],
            [sg.In()],
            [sg.Ok(), sg.Cancel()]], location=(0,0)).read(close=True)
    playlisturl = values[0] 
    playlistdir = values[1]
else:
# Pass the playlist URL and directory as arguments to the script call
    playlisturl = sys.argv[1]
    playlistdir = sys.argv[2]

theplaylist = '/home/john/Music/{}'.format(playlistdir)
# Create directory if not present
if not os.path.isdir(theplaylist):
    os.mkdir(theplaylist)

# Format filename for saved audio files
output = '{}/%(playlist_index)s-%(title)s.%(ext)s'.format(theplaylist)

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
