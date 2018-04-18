# Sound Analyzer

author: Patrick Stetz [(gihub)](https://github.com/pstetz)

# Introduction:

This project takes a .wav file and converts it to sheet music

# Important steps:

- Opens a wav file

- Segments the sound into notes

- Takes a fft and determines the note 

- Plots the note on sheet music.

# Advanced ideas:

- Determine dynamic (piano or forte)

- Able to convert mp3 files as well

- Able to handle multiple instruments

- Look at partials to determine the instrument

- Given sheet music outputs an wav/mp3 file


# Resources:

 - To interpret the output XML file please download [MuseScore's](https://musescore.org/en) free software

 - For a thorough understanding of Music XML, please follow this [link](https://wpmedia.musicxml.com/wp-content/uploads/2017/12/musicxml-tutorial.pdf?_ga=2.160318969.598454358.1523905769-1890310323.1523905769)

 - [Colah's blog](https://colah.github.io/) is a great resource for visualizing neural networks

 - Python's [speech recognition library](https://pypi.org/project/SpeechRecognition/) will be helpful once I start trying to get lyics

# Abandoned ideas:

- Create my own software that will plot the sheet music onto a staff and spit out a pdf instead of a music xml


