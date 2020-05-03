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

def the_gui():
    window = sg.Window('YTaudio',
            [[sg.Text('Playlist URL')],
            [sg.In()],
            [sg.Text('Directory Name')],
            [sg.In()],
            [sg.T('Window will close when downloads complete', size=(45,1))],
            [sg.Button('Go', bind_return_key=True), sg.Button('Close')]], location=(0,0)).Finalize()
    while True:
        event,values = window.read()
        if event in (None,'Close'):
            window.close()
            break
        plurl = values[0] 
        pldir = values[1]
        dlfunct(plurl,pldir)
        window.close()

if __name__ == '__main__':
    the_gui()
