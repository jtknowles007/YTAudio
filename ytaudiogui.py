#! /usr/bin/env python3

import os
import sys
import PySimpleGUI as sg
import youtube_dl

def dlfunct(playlisturl,playlistdir):
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
            'continue_dl':True,
            'ignoreerrors':True,
            'outtmpl':output}

        # Download and convert the Youtube audio
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.cache.remove()
            ydl.download([playlisturl])

window = sg.Window('YTaudio',
            [[sg.Text('Playlist URL')],
            [sg.In()],
            [sg.Text('Directory Name')],
            [sg.In()],
            [sg.Button('Go'), sg.Button('Close')]], location=(0,0))
while True:
    event,values = window.read()
    if event in (None,'Close'):
        break
    elif event in ('Go'):
        plurl = values[0] 
        pldir = values[1]
        dlfunct(plurl,pldir)
window.close()

