# YTAudio
Create mp3 files from Youtube playlists.

# Use:
Call the script with the Youtube playlist URL as [argv1] and the path/directory you wish to put the mp3 files in as [argv2].
```
./ytaudio.py [argv1] [argv2]
```

# Output
The script will use youtube_dl to download each video file in the playlist to the specified directory, then ffmpeg will convert the video to an mp3.  Once the conversion is complete, the video file is deleted.  Saved mp3 files are named as PlaylistIndex_Title.mp3

# Example:
```
./ytaudio.py https://www.youtube.com/watch?v=qeMFqkcPYcg&list=PLpYWKGMgRA1uU9lyMtR8vQBzc4HrjpqYu ~/Music/MyPlaylist
```


