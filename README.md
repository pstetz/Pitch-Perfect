# Sound Analyzer

author: Patrick Stetz [(gihub)](https://github.com/pstetz)

# Introduction:

This project takes a .wav music file and converts it to sheet music.

# Install:

### Clone repo unto your own folder

`git clone https://github.com/pstetz/sound_analyzer.git`

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

