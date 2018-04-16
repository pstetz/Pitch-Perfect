# Sound Analyzer

author: Patrick Stetz [gihub](https://github.com/pstetz)

# Introduction:

This project takes a .wav file and converts it to sheet music

# Important steps:

- Opens a wav file (would be great if it could convert a mp3 to wav)

- Segments the sound into notes (later be able to handle multiple instruments)

- Takes a fft and determines the note (look at partials to determine the instrument)

- Plots the note on sheet music.  There's an easy way and a hard way to do this.  The hard way is to essentially create my own software that will plot the sheet music onto a staff.  The "easy" way is to have python save the results into a music xml that can be read by Muse Score 2 (online for free).  I'm going with the easy way although it's not that easy if you take a look at how music xml are written.

# Advanced ideas:



