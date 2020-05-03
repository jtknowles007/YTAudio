#! /usr/bin/env python3

import os
import sys
import queue
import threading
import PySimpleGUI as sg
import youtube_dl

def dlfunct(playlisturl,playlistdir,q):
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
            q.put('Remove cache')
            q.put('Begin downloads')
            ydl.download([playlisturl])
            q.put('Complete')

def the_gui():
    sg.theme('Light Brown 3')
    gui_queue = queue.Queue()
    window = sg.Window('YTaudio',
            [[sg.Text('Playlist URL')],
            [sg.In()],
            [sg.Text('Directory Name')],
            [sg.In()],
            [sg.Output(size=(70, 12),key='outkey')],
            [sg.Button('Run', bind_return_key=True), sg.Button('Close')]], location=(0,0))
    while True:
        event,values = window.read(timeout=100)
        if event in (None,'Close'):
            window.close()
            break
        elif event == 'Run':
            plurl = values[0] 
            pldir = values[1]
            threading.Thread(target=dlfunct, args=(plurl,pldir,gui_queue,),daemon=True).start()
        try:
            message = gui_queue.get_nowait()
        except queue.Empty:
            message = None
        if message:
            print(message)
    window.close()
    

if __name__ == '__main__':
    the_gui()
