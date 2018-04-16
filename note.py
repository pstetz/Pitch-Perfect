class Note:
    
    def __init__(self, note="A", octave=3, duration=4, typ="whole", pitch="440"):
        self.note = note
        self.octave = octave
        self.duration = duration
        self.typ = typ
        self.pitch = pitch