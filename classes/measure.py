class Measure:
    
    def __init__(self, number, line=2, beats=4, beat_type=4, sign="G", divisions=1, new_attributes=False):
        self.number = number
        self.line = line
        self.beats = beats
        self.beat_type = beat_type
        self.sign = sign
        self.divisions = divisions
        self.new_attributes = (number == 1)
        self.notes = list()
        
    def addNote(self, note):
        self.notes.append(note)
        