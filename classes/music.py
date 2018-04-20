# general imports
import numpy as np

# scipy imports
from scipy.fftpack import fft
from scipy.io import wavfile

# custom classes
from measure import Measure
from note import Note

class Music:
    
    def __init__(self, 
                 title="title",
                 artist="Patrick Stetz",
                 time_signature=(4, 4),
                 tempo=60,
                 ver_number="0.00"):
            
        self.title = title
        self.artist = artist
        self.time_signature = time_signature
        self.tempo = tempo
        self.ver_number = ver_number # version number of decoder

    def read(self, input_path, is_wav_format=True):
        self.input_path = input_path
        if is_wav_format:
            self.sample_rate, self.raw = wavfile.read(input_path)
        self.chan1, self.chan2 = zip(*self.raw)
        
    def compile_music(self, window=1000, DIFF=15):
        self.measures = list()
        
        peaks = self.find_peaks(window, DIFF)
        notes = self.get_notes(peaks)
        notes = self.filter_notes(notes)
        for i, note in enumerate(notes):
            measure = Measure(i+1)
            measure.addNote(note)
            self.addMeasure(measure)
        return notes
    
    def get_notes(self, peaks, inspection_width=10000, use_chan1=True):
        ret = list()
        for peak in peaks:
            if use_chan1:
                inspection_zone = self.chan1[peak: peak+inspection_width]
                fft_data = np.abs(fft(inspection_zone))
                
                conversion_factor = self.sample_rate / len(fft_data)
                max_signal = max(fft_data)
                resonant_freqs = (-fft_data).argsort()
                timestamp = peak / self.sample_rate

                for freq in resonant_freqs:
                    if fft_data[freq] < max_signal * 0.25:
                        break
                    note = fft_data[freq] * conversion_factor
                    note = Note(note, timestamp)
                    ret.append(note)
        return ret

    # ideally this is when dynamics will come in
    def filter_notes(self, notes):
        N = len(notes)
        to_delete = list()
        for i in range(1, N):
            if notes[i - 1].given_pitch == notes[i].given_pitch:
                to_delete.append(i)
        for index in list(reversed(to_delete)):
            del notes[index]
        return notes
            
        
    
    # Maybe there's a less computationally expensive way to find the start of notes instead of standard deviation?
    def find_peaks(self, window, DIFF):
        peaks = list()
        for i in range(window, len(self.chan1) - window, window):
            prev = self.chan1[i-window: i]
            curr = self.chan1[i: i+window]
            p_std = np.std(prev)
            c_std = np.std(curr)
            if c_std > p_std + DIFF:
                peaks.append(i)
        return peaks
        
    def addMeasure(self, measure):
        self.measures.append(measure)
        
    def save(self, output_path):

        file = open(output_path, "w") 

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
            file.write('    <measure number="{}">\n'.format(measure.number))
            if measure.new_attributes:
                file.write('      <attributes>\n')
                file.write('        <divisions>{}</divisions>\n'.format(measure.divisions))
                file.write('        <key><fifths>0</fifths></key>\n') # FIXME: look into this
                file.write('        <time>\n')
                file.write('          <beats>{}</beats>\n'.format(measure.beats))
                file.write('          <beat-type>{}</beat-type>\n'.format(measure.beat_type))
                file.write('        </time>\n')
                file.write('        <clef>\n')
                file.write('          <sign>{}</sign>\n'.format(measure.sign))
                file.write('          <line>{}</line>\n'.format(measure.line))
                file.write('        </clef>\n')
                file.write('      </attributes>\n')

            # writes notes from spefic measure
            for note in measure.notes:
                file.write('      <note>\n')
                file.write('        <pitch>\n')
                file.write('          <step>{}</step>\n'.format(note.note))
                file.write('          <alter>{}</alter>\n'.format(note.alter))               
                file.write('          <octave>{}</octave>\n'.format(note.octave))
                file.write('        </pitch>\n')
                file.write('        <duration>{}</duration>\n'.format(note.duration))
                file.write('        <type>{}</type>\n'.format(note.typ))
                file.write('      </note>\n')

            file.write('    </measure>\n')

        # write bottom
        file.write('  </part>\n')
        file.write('</score-partwise>\n')

        file.close() 
