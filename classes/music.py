class Music:
    
    # FIXME: make all these inputs mandatory
    def __init__(self, title="title", author="Patrick Stetz",
                 output_path="/Users/pbezuhov/Desktop/output.xml", input_path="input",
                 ver_number="0.00"):
        self.title = title
        self.output_path = output_path
        self.input_path = input_path
        self.author = author
        self.ver_number = ver_number # version number of decoder
        self.measures = list()
        
    def addMeasure(self, measure):
        self.measures.append(measure)
        
    def saveFile(self):
        file = open(self.output_path, "w") 

        # write top
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        file.write('<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n')
        file.write('<score-partwise version="3.1">\n')
        file.write('  <part-list>\n')
        file.write('    <score-part id="P1">\n')
        file.write('      <part-name>{}</part-name>\n'.format(self.title))
        file.write('    </score-part>\n')
        file.write('  </part-list>\n')
        file.write('  <part id="P1">\n')

        # write first measure

        # create music
        for measure in self.measures:
            file.write('  <measure number="{}">\n'.format(measure.number))
            if measure.new_attributes:
                file.write('    <attributes>\n')
                file.write('      <divisions>{}</divisions>\n'.format(measure.divisions))
                file.write('      <key><fifths>0</fifths></key>\n') # FIXME: look into this
                file.write('      <time>\n')
                file.write('        <beats>{}</beats>\n'.format(measure.beats))
                file.write('        <beat-type>{}</beat-type>\n'.format(measure.beat_type))
                file.write('      </time>\n')
                file.write('      <clef>\n')
                file.write('        <sign>{}</sign>\n'.format(measure.sign))
                file.write('        <line>{}</line>\n'.format(measure.line))
                file.write('      </clef>\n')
                file.write('    </attributes>\n')

            # writes notes from spefic measure
            for note in measure.notes:
                file.write('    <note>\n')
                file.write('      <pitch>\n')
                file.write('        <step>{}</step>\n'.format(note.note))
                file.write('        <octave>{}</octave>\n'.format(note.octave))
                file.write('      </pitch>\n')
                file.write('      <duration>{}</duration>\n'.format(note.duration))
                file.write('      <type>{}</type>\n'.format(note.typ))
                file.write('    </note>\n')

            file.write('  </measure>\n')

        # write bottom
        file.write('  </part>\n')
        file.write('</score-partwise>\n')

        file.close() 
