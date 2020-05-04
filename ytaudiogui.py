#! /usr/bin/env python3

import os
import sys
import queue
import threading
import PySimpleGUI as sg
import youtube_dl
import polymodule as pm

def getcolors():
    colordict = {}
    for i in range(0,16):
        thecolor = "color" + str(i)
        colordict[thecolor] = pm.pycolors(thecolor)
    return colordict

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
    sg.theme('Light Grey 3')
    sg.theme_background_color(colors['color0'])
    sg.theme_text_element_background_color(colors['color0'])
    sg.theme_input_background_color(colors['color8'])
    sg.theme_text_color(colors['color7'])
    sg.theme_input_text_color(colors['color0'])
    sg.theme_button_color((colors['color0'],colors['color4']))

    

    gui_queue = queue.Queue()
    window = sg.Window('YTaudio',
            [
            [sg.Text('YTAudio', font='Hack 14')],
            [sg.Text('Generate MP3s from Youtube Playlists')],
            [sg.Text('Enter Youtube Playlist URL')],
            [sg.In()],
            [sg.Text('Enter Name of Save Directory')],
            [sg.In()],
            [sg.Text('Download and Conversion Status')],
            [sg.Output(size=(45, 5),key='outkey')],
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
    colors = getcolors()
    the_gui()
