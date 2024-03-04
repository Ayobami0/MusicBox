# MusicBox
##### A music player for your command line built with python.

![MusicBox](./screenshots/screenshot1.png "MusicBox")

### Description
___
MusicBox is a command line music player built completely with python programming language - Using the cmd, pygame, mutagen and other packages.

The implementation of MusicBox offers a simple text interface to interact with mp3 music files on your pc.

This project is built as the foundations portfolio and collaboration project assigned by ALX

### Installation
___
Requirements: python >= 3.8, pip, pygame, mutagen
##### Clone repsitory
```
git clone {{url}} MusicBox 
cd MusicBox
```
##### Install requirements
```
pip install -r requirements.txt
```
##### Run it
```
python main.py
```

### Usage
___
1. Play multiple song files
```
> play file1.mp3 file2.mp3 file3.mp3
```
2. Add songs to queue then play them
```
> queue file1.mp3 file2.mp3 file3.mp3
> play
```
3. Add a preset directory to lookup songs
```
> preset dir1 dir2
```
4. Pause and Resume playback of a song
```
> pause
> resume
```
5. Show the information on a song
```
> info song.mp3
===============================
song.mp3
TITLE  : A Song
ARTIST : Singer
LENGTH : 0:02:30
ALBUM  : An Album
TRACK  : 99
===============================
```
