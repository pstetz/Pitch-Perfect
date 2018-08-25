# maybe don't need?
from note import Note

class Measure:
    
    def __init__(self, number, beats, beat_type, line=4, clef="bass", divisions=1, new_attributes=False):
        self.number = number + 1
        self.divisions = divisions
        self.new_attributes = (self.number == 1)
        
        self.beats = beats
        self.beat_type = beat_type
        clefInfo = self.getClef(clef)
        self.line = clefInfo["line"]
        self.sign = clefInfo["sign"]
        self.beats_left = beats
        self.notes = list()
        
    def addNote(self, note):
        """
        Adds a note to the measure.
        
        NOTE: Does not perform any checks before adding the note.
        """
        self.notes.append(note)
        
    def wrap_up_time(self):
        """
        TODO: Fills the remaining space in a measure with empty time.
        """
        pass
        
    def getClef(self, clef):
        """
        Returns the information for a particular cleft.  This is only important for XML formatting.
        """
        return {
                "treble": {"sign": "G", "line": 2},
                "alto":   {"sign": "C", "line": 3},
                "bass":   {"sign": "F", "line": 4}
               }[clef]
    