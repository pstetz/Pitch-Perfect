# Sound Analyzer

author: Patrick Stetz [(gihub)](https://github.com/pstetz)

# Introduction:

This project takes a .wav file and converts it to sheet music.  This project is in it's beginnings so it can only transcript 1 or 2 notes at a time and cannot differentiate between instruments.

# Install:

### Clone repo unto your own folder

`https://github.com/pstetz/sound_analyzer.git`

### Open main.ipynb

- Fill in appropriate variables like input file (music being transcribed) and output path (for the sheet music)

### Download [MuseScore](https://musescore.org/en) to read new music XML file

# Background:

## Method 1: FFT

1.) Segments sound file into likely candidates for notes.

2.) Each note is individually looked at through Fast Fourier Transform.

3.) The different frequencies are looked at to see if multiple notes were played at a time

4.) The duration of the note is determined either by how long it takes to get to the 25% loudness mark or until the next note is played

## Method 2: RNN

Not yet operable

# Resources:

 - For a thorough understanding of Music XML, please follow this [link](https://wpmedia.musicxml.com/wp-content/uploads/2017/12/musicxml-tutorial.pdf?_ga=2.160318969.598454358.1523905769-1890310323.1523905769)

 - [Colah's blog](https://colah.github.io/) is a great resource for visualizing neural networks

 - Python's [speech recognition library](https://pypi.org/project/SpeechRecognition/) will be helpful once I start trying to get lyics



