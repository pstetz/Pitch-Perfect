import numpy as np
from info import freq_to_notes

class Note:
    
    def __init__(self, pitch, signal, loudness, timestamp, duration=None, typ=None):
        self.pitch       = round(pitch, 3)
        self.signal      = round(signal, 3)
        self.loudness    = round(loudness, 3)
        self.timestamp   = timestamp
        self.given_pitch = self.closest_pitch(pitch)
        
        self.duration = duration
        self.typ      = typ
        
        note_info   = freq_to_notes[self.given_pitch]
        self.id     = note_info["id"]
        self.note   = note_info["note"]
        self.octave = note_info["octave"]
        self.alter  = note_info["alter"]
        
    def closest_pitch(self, pitch):
        """
        Given a pitch finds the closest musical note.  This is determined by the absolute distance in frequency (Hertz).
        """
        pitches = np.array(list(freq_to_notes.keys()))
        idx     = (np.abs(pitches - pitch)).argmin()
        return pitches[idx]
    
    def getInfo(self):
        """
        Returns all the information stored in a musical note.
        """
        return (self.timestamp, self.id, self.signal, self.pitch, self.given_pitch,
                self.loudness, self.note, self.octave, self.alter)
    
    def describe(self):
        """
        Prints all the information describing a note.
        """
        note  = str(self.note)
        note += ("#" if self.alter else "")
        print(f"\n{note}, octave: {self.octave}, actual pitch: {self.pitch}Hz, ideal pitch: {self.given_pitch}Hz")
        print(f"timestamp: {self.timestamp}")
