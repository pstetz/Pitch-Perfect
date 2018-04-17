import numpy as np

class Note:
    
    def __init__(self, pitch, duration=4, typ="whole"):
        self.pitch = pitch
        self.duration = duration
        self.typ = typ
        self.given_pitch = self.closest_pitch(pitch)
        
        note_info = freq_to_notes[self.given_pitch]
        self.note   = note_info["note"]
        self.octave = note_info["octave"]
        self.alter  = note_info["alter"]
        
    def closest_pitch(self, pitch):
        pitches = np.array(list(freq_to_notes.keys()))
        idx = (np.abs(pitches - pitch)).argmin()
        return pitches[idx]
    
    def describe(self):
        note = str(self.note)
        note += ("#" if self.alter else "")
        print("{}, octave: {}, actual pitch: {}Hz, ideal pitch: {}Hz".format(note, self.octave, self.pitch, self.given_pitch))
        
freq_to_notes = {
    
    # octave 0
    16.35: {"note": "C", "octave": 0, "alter": 0},
    17.32: {"note": "C", "octave": 0, "alter": 1},
    18.35: {"note": "D", "octave": 0, "alter": 0},
    19.45: {"note": "D", "octave": 0, "alter": 1},
    20.60: {"note": "E", "octave": 0, "alter": 0},
    21.83: {"note": "F", "octave": 0, "alter": 0},
    23.12: {"note": "F", "octave": 0, "alter": 1},
    24.50: {"note": "G", "octave": 0, "alter": 0},
    25.96: {"note": "G", "octave": 0, "alter": 1},
    27.50: {"note": "A", "octave": 0, "alter": 0},
    29.14: {"note": "A", "octave": 0, "alter": 1},
    30.87: {"note": "B", "octave": 0, "alter": 0},
    
    # octave 1
    32.70: {"note": "C", "octave": 1, "alter": 0},
    34.65: {"note": "C", "octave": 1, "alter": 1},
    36.71: {"note": "D", "octave": 1, "alter": 0},
    38.89: {"note": "D", "octave": 1, "alter": 1},
    41.20: {"note": "E", "octave": 1, "alter": 0},
    43.65: {"note": "F", "octave": 1, "alter": 0},
    46.25: {"note": "F", "octave": 1, "alter": 1},
    49.00: {"note": "G", "octave": 1, "alter": 0},
    51.91: {"note": "G", "octave": 1, "alter": 1},
    55.00: {"note": "A", "octave": 1, "alter": 0},
    58.27: {"note": "A", "octave": 1, "alter": 1},
    61.74: {"note": "B", "octave": 1, "alter": 0},
    
    # octave 2
    65.410: {"note": "C", "octave": 2, "alter": 0},
    69.300: {"note": "C", "octave": 2, "alter": 1},
    73.420: {"note": "D", "octave": 2, "alter": 0},
    77.780: {"note": "D", "octave": 2, "alter": 1},
    82.410: {"note": "E", "octave": 2, "alter": 0},
    87.310: {"note": "F", "octave": 2, "alter": 0},
    92.500: {"note": "F", "octave": 2, "alter": 1},
    98.000: {"note": "G", "octave": 2, "alter": 0},
    103.83: {"note": "G", "octave": 2, "alter": 1},
    110.00: {"note": "A", "octave": 2, "alter": 0},
    116.54: {"note": "A", "octave": 2, "alter": 1},
    123.47: {"note": "B", "octave": 2, "alter": 0},
    
    # octave 3
    130.81: {"note": "C", "octave": 3, "alter": 0},
    138.59: {"note": "C", "octave": 3, "alter": 1},
    146.83: {"note": "D", "octave": 3, "alter": 0},
    155.56: {"note": "D", "octave": 3, "alter": 1},
    164.81: {"note": "E", "octave": 3, "alter": 0},
    174.61: {"note": "F", "octave": 3, "alter": 0},
    185.00: {"note": "F", "octave": 3, "alter": 1},
    196.00: {"note": "G", "octave": 3, "alter": 0},
    207.65: {"note": "G", "octave": 3, "alter": 1},
    220.00: {"note": "A", "octave": 3, "alter": 0},
    233.08: {"note": "A", "octave": 3, "alter": 1},
    246.94: {"note": "B", "octave": 3, "alter": 0},
    
    # octave 4
    261.63: {"note": "C", "octave": 4, "alter": 0},
    277.18: {"note": "C", "octave": 4, "alter": 1},
    293.66: {"note": "D", "octave": 4, "alter": 0},
    311.13: {"note": "D", "octave": 4, "alter": 1},
    329.63: {"note": "E", "octave": 4, "alter": 0},
    349.23: {"note": "F", "octave": 4, "alter": 0},
    369.99: {"note": "F", "octave": 4, "alter": 1},
    392.00: {"note": "G", "octave": 4, "alter": 0},
    415.30: {"note": "G", "octave": 4, "alter": 1},
    440.00: {"note": "A", "octave": 4, "alter": 0},
    466.16: {"note": "A", "octave": 4, "alter": 1},
    493.88: {"note": "B", "octave": 4, "alter": 0},
    
    # octave 5
    523.25: {"note": "C", "octave": 5, "alter": 0},
    554.37: {"note": "C", "octave": 5, "alter": 1},
    587.33: {"note": "D", "octave": 5, "alter": 0},
    622.25: {"note": "D", "octave": 5, "alter": 1},
    659.25: {"note": "E", "octave": 5, "alter": 0},
    698.46: {"note": "F", "octave": 5, "alter": 0},
    739.99: {"note": "F", "octave": 5, "alter": 1},
    783.99: {"note": "G", "octave": 5, "alter": 0},
    830.61: {"note": "G", "octave": 5, "alter": 1},
    880.00: {"note": "A", "octave": 5, "alter": 0},
    932.33: {"note": "A", "octave": 5, "alter": 1},
    987.77: {"note": "B", "octave": 5, "alter": 0},
    
    # octave 6
    1046.50: {"note": "C", "octave": 6, "alter": 0},
    1108.73: {"note": "C", "octave": 6, "alter": 1},
    1174.66: {"note": "D", "octave": 6, "alter": 0},
    1244.51: {"note": "D", "octave": 6, "alter": 1},
    1318.51: {"note": "E", "octave": 6, "alter": 0},
    1396.91: {"note": "F", "octave": 6, "alter": 0},
    1479.98: {"note": "F", "octave": 6, "alter": 1},
    1567.98: {"note": "G", "octave": 6, "alter": 0},
    1661.22: {"note": "G", "octave": 6, "alter": 1},
    1760.00: {"note": "A", "octave": 6, "alter": 0},
    1864.66: {"note": "A", "octave": 6, "alter": 1},
    1975.53: {"note": "B", "octave": 6, "alter": 0},
    
    # octave 7
    2093.00: {"note": "C", "octave": 7, "alter": 0},
    2217.46: {"note": "C", "octave": 7, "alter": 1},
    2349.32: {"note": "D", "octave": 7, "alter": 0},
    2489.02: {"note": "D", "octave": 7, "alter": 1},
    2637.02: {"note": "E", "octave": 7, "alter": 0},
    2793.83: {"note": "F", "octave": 7, "alter": 0},
    2959.96: {"note": "F", "octave": 7, "alter": 1},
    3135.96: {"note": "G", "octave": 7, "alter": 0},
    3322.44: {"note": "G", "octave": 7, "alter": 1},
    3520.00: {"note": "A", "octave": 7, "alter": 0},
    3729.31: {"note": "A", "octave": 7, "alter": 1},
    3951.07: {"note": "B", "octave": 7, "alter": 0},
    
    # octave 8
    4186.01: {"note": "C", "octave": 8, "alter": 0},
    4434.92: {"note": "C", "octave": 8, "alter": 1},
    4698.63: {"note": "D", "octave": 8, "alter": 0},
    4978.03: {"note": "D", "octave": 8, "alter": 1},
    5274.04: {"note": "E", "octave": 8, "alter": 0},
    5587.65: {"note": "F", "octave": 8, "alter": 0},
    5919.91: {"note": "F", "octave": 8, "alter": 1},
    6271.93: {"note": "G", "octave": 8, "alter": 0},
    6644.88: {"note": "G", "octave": 8, "alter": 1},
    7040.00: {"note": "A", "octave": 8, "alter": 0},
    7458.62: {"note": "A", "octave": 8, "alter": 1},
    7902.13: {"note": "B", "octave": 8, "alter": 0},
}