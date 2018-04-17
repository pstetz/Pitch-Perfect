# maybe don't need?
from note import Note

class Measure:
    
    def __init__(self, number, line=4, clef="bass", beats=4, beat_type=4, divisions=1, new_attributes=False):
        self.number = number
        self.divisions = divisions
        self.new_attributes = (number == 1)
        
        self.beats = beats
        self.beat_type = beat_type
        clefInfo = self.getClef(clef)
        self.line = clefInfo["line"]
        self.sign = clefInfo["sign"]
        
        self.notes = list()
        
    def addNote(self, note):
        self.notes.append(note)
        
    def getClef(self, clef):
        return {
                "treble": {"sign": "G", "line": 2},
                "alto":   {"sign": "C", "line": 3},
                "bass":   {"sign": "F", "line": 4}
               }[clef]
    