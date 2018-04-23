import numpy as np

class Note:
    
    def __init__(self, pitch, signal, loudness, timestamp, duration=4, typ="whole"):
        self.pitch = round(pitch, 3)
        self.signal = round(signal, 3)
        self.loudness = round(loudness, 3)
        self.timestamp = timestamp
        self.duration = duration
        self.typ = typ
        self.given_pitch = self.closest_pitch(pitch)
        
        note_info = freq_to_notes[self.given_pitch]
        self.id     = note_info["id"]
        self.note   = note_info["note"]
        self.octave = note_info["octave"]
        self.alter  = note_info["alter"]
        
    def closest_pitch(self, pitch):
        pitches = np.array(list(freq_to_notes.keys()))
        idx = (np.abs(pitches - pitch)).argmin()
        return pitches[idx]
    
    def getInfo(self):
        return (self.timestamp, self.id, self.signal, self.pitch, self.given_pitch,
                self.loudness, self.duration, self.note, self.octave, self.alter)
    
    def describe(self):
        note = str(self.note)
        note += ("#" if self.alter else "")
        print("\n{}, octave: {}, actual pitch: {}Hz, ideal pitch: {}Hz".format(note, self.octave, self.pitch, self.given_pitch))
        print("timestamp: {}".format(self.timestamp))
        
freq_to_notes = {
    
    # octave 0
    16.35: {"note": "C", "octave": 0, "alter": 0, "id": 1},
    17.32: {"note": "C", "octave": 0, "alter": 1, "id": 2},
    18.35: {"note": "D", "octave": 0, "alter": 0, "id": 3},
    19.45: {"note": "D", "octave": 0, "alter": 1, "id": 4},
    20.60: {"note": "E", "octave": 0, "alter": 0, "id": 5},
    21.83: {"note": "F", "octave": 0, "alter": 0, "id": 6},
    23.12: {"note": "F", "octave": 0, "alter": 1, "id": 7},
    24.50: {"note": "G", "octave": 0, "alter": 0, "id": 8},
    25.96: {"note": "G", "octave": 0, "alter": 1, "id": 9},
    27.50: {"note": "A", "octave": 0, "alter": 0, "id": 10},
    29.14: {"note": "A", "octave": 0, "alter": 1, "id": 11},
    30.87: {"note": "B", "octave": 0, "alter": 0, "id": 12},
    
    # octave 1
    32.70: {"note": "C", "octave": 1, "alter": 0, "id": 13},
    34.65: {"note": "C", "octave": 1, "alter": 1, "id": 14},
    36.71: {"note": "D", "octave": 1, "alter": 0, "id": 15},
    38.89: {"note": "D", "octave": 1, "alter": 1, "id": 16},
    41.20: {"note": "E", "octave": 1, "alter": 0, "id": 17},
    43.65: {"note": "F", "octave": 1, "alter": 0, "id": 18},
    46.25: {"note": "F", "octave": 1, "alter": 1, "id": 19},
    49.00: {"note": "G", "octave": 1, "alter": 0, "id": 20},
    51.91: {"note": "G", "octave": 1, "alter": 1, "id": 21},
    55.00: {"note": "A", "octave": 1, "alter": 0, "id": 22},
    58.27: {"note": "A", "octave": 1, "alter": 1, "id": 23},
    61.74: {"note": "B", "octave": 1, "alter": 0, "id": 24},
    
    # octave 2
    65.410: {"note": "C", "octave": 2, "alter": 0, "id": 25},
    69.300: {"note": "C", "octave": 2, "alter": 1, "id": 26},
    73.420: {"note": "D", "octave": 2, "alter": 0, "id": 27},
    77.780: {"note": "D", "octave": 2, "alter": 1, "id": 28},
    82.410: {"note": "E", "octave": 2, "alter": 0, "id": 29},
    87.310: {"note": "F", "octave": 2, "alter": 0, "id": 30},
    92.500: {"note": "F", "octave": 2, "alter": 1, "id": 31},
    98.000: {"note": "G", "octave": 2, "alter": 0, "id": 32},
    103.83: {"note": "G", "octave": 2, "alter": 1, "id": 33},
    110.00: {"note": "A", "octave": 2, "alter": 0, "id": 34},
    116.54: {"note": "A", "octave": 2, "alter": 1, "id": 35},
    123.47: {"note": "B", "octave": 2, "alter": 0, "id": 36},
    
    # octave 3
    130.81: {"note": "C", "octave": 3, "alter": 0, "id": 37},
    138.59: {"note": "C", "octave": 3, "alter": 1, "id": 38},
    146.83: {"note": "D", "octave": 3, "alter": 0, "id": 39},
    155.56: {"note": "D", "octave": 3, "alter": 1, "id": 40},
    164.81: {"note": "E", "octave": 3, "alter": 0, "id": 41},
    174.61: {"note": "F", "octave": 3, "alter": 0, "id": 42},
    185.00: {"note": "F", "octave": 3, "alter": 1, "id": 43},
    196.00: {"note": "G", "octave": 3, "alter": 0, "id": 44},
    207.65: {"note": "G", "octave": 3, "alter": 1, "id": 45},
    220.00: {"note": "A", "octave": 3, "alter": 0, "id": 46},
    233.08: {"note": "A", "octave": 3, "alter": 1, "id": 47},
    246.94: {"note": "B", "octave": 3, "alter": 0, "id": 48},
    
    # octave 4
    261.63: {"note": "C", "octave": 4, "alter": 0, "id": 49},
    277.18: {"note": "C", "octave": 4, "alter": 1, "id": 50},
    293.66: {"note": "D", "octave": 4, "alter": 0, "id": 51},
    311.13: {"note": "D", "octave": 4, "alter": 1, "id": 52},
    329.63: {"note": "E", "octave": 4, "alter": 0, "id": 53},
    349.23: {"note": "F", "octave": 4, "alter": 0, "id": 54},
    369.99: {"note": "F", "octave": 4, "alter": 1, "id": 55},
    392.00: {"note": "G", "octave": 4, "alter": 0, "id": 56},
    415.30: {"note": "G", "octave": 4, "alter": 1, "id": 57},
    440.00: {"note": "A", "octave": 4, "alter": 0, "id": 58},
    466.16: {"note": "A", "octave": 4, "alter": 1, "id": 59},
    493.88: {"note": "B", "octave": 4, "alter": 0, "id": 60},
    
    # octave 5
    523.25: {"note": "C", "octave": 5, "alter": 0, "id": 61},
    554.37: {"note": "C", "octave": 5, "alter": 1, "id": 62},
    587.33: {"note": "D", "octave": 5, "alter": 0, "id": 63},
    622.25: {"note": "D", "octave": 5, "alter": 1, "id": 64},
    659.25: {"note": "E", "octave": 5, "alter": 0, "id": 65},
    698.46: {"note": "F", "octave": 5, "alter": 0, "id": 66},
    739.99: {"note": "F", "octave": 5, "alter": 1, "id": 67},
    783.99: {"note": "G", "octave": 5, "alter": 0, "id": 68},
    830.61: {"note": "G", "octave": 5, "alter": 1, "id": 69},
    880.00: {"note": "A", "octave": 5, "alter": 0, "id": 70},
    932.33: {"note": "A", "octave": 5, "alter": 1, "id": 71},
    987.77: {"note": "B", "octave": 5, "alter": 0, "id": 72},
    
    # octave 6
    1046.50: {"note": "C", "octave": 6, "alter": 0, "id": 73},
    1108.73: {"note": "C", "octave": 6, "alter": 1, "id": 74},
    1174.66: {"note": "D", "octave": 6, "alter": 0, "id": 75},
    1244.51: {"note": "D", "octave": 6, "alter": 1, "id": 76},
    1318.51: {"note": "E", "octave": 6, "alter": 0, "id": 77},
    1396.91: {"note": "F", "octave": 6, "alter": 0, "id": 78},
    1479.98: {"note": "F", "octave": 6, "alter": 1, "id": 79},
    1567.98: {"note": "G", "octave": 6, "alter": 0, "id": 80},
    1661.22: {"note": "G", "octave": 6, "alter": 1, "id": 81},
    1760.00: {"note": "A", "octave": 6, "alter": 0, "id": 82},
    1864.66: {"note": "A", "octave": 6, "alter": 1, "id": 83},
    1975.53: {"note": "B", "octave": 6, "alter": 0, "id": 84},
    
    # octave 7
    2093.00: {"note": "C", "octave": 7, "alter": 0, "id": 85},
    2217.46: {"note": "C", "octave": 7, "alter": 1, "id": 86},
    2349.32: {"note": "D", "octave": 7, "alter": 0, "id": 87},
    2489.02: {"note": "D", "octave": 7, "alter": 1, "id": 88},
    2637.02: {"note": "E", "octave": 7, "alter": 0, "id": 89},
    2793.83: {"note": "F", "octave": 7, "alter": 0, "id": 90},
    2959.96: {"note": "F", "octave": 7, "alter": 1, "id": 91},
    3135.96: {"note": "G", "octave": 7, "alter": 0, "id": 92},
    3322.44: {"note": "G", "octave": 7, "alter": 1, "id": 93},
    3520.00: {"note": "A", "octave": 7, "alter": 0, "id": 94},
    3729.31: {"note": "A", "octave": 7, "alter": 1, "id": 95},
    3951.07: {"note": "B", "octave": 7, "alter": 0, "id": 96},
    
    # octave 8
    4186.01: {"note": "C", "octave": 8, "alter": 0, "id": 97},
    4434.92: {"note": "C", "octave": 8, "alter": 1, "id": 98},
    4698.63: {"note": "D", "octave": 8, "alter": 0, "id": 99},
    4978.03: {"note": "D", "octave": 8, "alter": 1, "id": 100},
    5274.04: {"note": "E", "octave": 8, "alter": 0, "id": 101},
    5587.65: {"note": "F", "octave": 8, "alter": 0, "id": 102},
    5919.91: {"note": "F", "octave": 8, "alter": 1, "id": 103},
    6271.93: {"note": "G", "octave": 8, "alter": 0, "id": 104},
    6644.88: {"note": "G", "octave": 8, "alter": 1, "id": 105},
    7040.00: {"note": "A", "octave": 8, "alter": 0, "id": 106},
    7458.62: {"note": "A", "octave": 8, "alter": 1, "id": 107},
    7902.13: {"note": "B", "octave": 8, "alter": 0, "id": 108},
}