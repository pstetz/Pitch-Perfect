# general imports
import numpy as np
import pandas as pd

# scipy imports
from scipy.fftpack import fft
from scipy.io import wavfile

# custom classes
from measure import Measure
from note import Note
from info import duration_to_notes


def closest_duration(duration):
    durations = np.array(list(duration_to_notes.keys()))
    idx = (np.abs(durations - duration)).argmin()
    return durations[idx]

class Music:
    
    def __init__(self, 
                 title="Solitude in E minor",
                 artist="Patrick Stetz",
                 time_signature=(4, 4),
                 tempo=120,
                 ver_number="0.00"):
            
        self.title = title
        self.artist = artist
            
        self.time_signature = time_signature
        self.tempo = tempo
        self.unit = 60 / (tempo * 4) # Finest resolution is 16th notes
        self.unit_duration = tempo / 60
        self.ver_number = ver_number # version number of decoder
        
    def find_peaks(self, sound, separation, min_volume_level):

        # return value of peak positions and signal strength
        peaks = list()

        # initializing variables
        max_prev_i = np.argmax(sound[:separation])
        max_next_i = np.argmax(sound[separation + 1: 2 * separation]) + separation + 1
        max_prev   = sound[max_prev_i]
        max_next   = sound[max_next_i]

        for i in range(separation, len(sound) - separation - 1):

            # Determining the maximum value in the previous window
            if sound[i - 1] > max_prev:
                max_prev_i = i - 1
                max_prev   = sound[max_prev_i]
            elif i - max_prev_i > separation:
                max_prev_i = np.argmax(sound[i - separation: i - 1]) + i - separation
                max_prev   = sound[max_prev_i]

            # Determining the maximum value in the next window
            if sound[i + separation + 1] > max_next:
                max_next_i = i + separation + 1
                max_next   = sound[max_next_i]
            elif max_next_i == i:
                max_next_i = np.argmax(sound[i + 1: i + separation + 1]) + i + 1
                max_next = sound[max_next_i]

            # Determining if the current point is a peak
            if sound[i] > max_prev and sound[i] > max_next and sound[i] > min_volume_level:
                if len(peaks) == 0 or i - peaks[-1][0] > separation:
                    peaks.append((i, sound[i]))
        return peaks

    def read(self, input_path, is_wav_format=True):
        self.input_path = input_path
        if is_wav_format:
            self.sample_rate, self.raw = wavfile.read(input_path)
        self.chan1, self.chan2 = list(map(list, zip(*self.raw)))
        self.duration = len(self.raw) / self.sample_rate
        
    def get_input_path(self):
        return self.input_path
        
    def compile_music(self, separation=3000, min_volume_level=5000, max_pitch=4000, stength_cutoff=0.75, use_chan1=True):
        self.measures = list()
        
        if use_chan1:
            peaks = self.find_peaks(self.chan1, separation, min_volume_level)
            notes = self.get_notes(self.chan1, peaks, separation, max_pitch, stength_cutoff)
        notes = self.filter_groups(notes)
        notes = self.filter_nearby_times(notes)
        return notes
    
    def get_notes(self, sound, peaks, separation, max_pitch, stength_cutoff):
        notes = list()
        for peak, loudness in peaks:
            
            inspection_zone = sound[peak: peak + separation]
            fft_data = np.abs(fft(inspection_zone))

            conversion_factor = self.sample_rate / len(fft_data)
            max_signal = max(fft_data)
            resonant_freqs = (-fft_data).argsort()
            timestamp = peak / self.sample_rate

            for freq in resonant_freqs:
                signal = fft_data[freq]
                if signal < stength_cutoff * max_signal:
                    break
                if freq * conversion_factor < max_pitch:
                    note = Note(freq * conversion_factor, signal, loudness, timestamp)
                    notes.append(note.getInfo())
        notes = pd.DataFrame(notes, columns=["time", "id", "signal", "pitch", "given_pitch",
                                             "loudness", "note", "octave", "alter"])
        return notes

    # picks the loudest frequency for a certain time
    def filter_groups(self, notes):
        ret = pd.DataFrame(columns=notes.columns)
        groups = notes.groupby("time")

        for key, note in groups:
            
            if len(note) == 1:
                ret = ret.append(note)
            else:
                to_delete = list()
                index_offset = min(note.index)
                for i in range(index_offset, len(note) + index_offset):
                    for j in range(i + 1, len(note) + index_offset):
#                         if abs(note.id[i] - note.id[j]) < 2:
                        to_delete.append(i if note.loudness[i] < note.loudness[j] else j)
                ret = ret.append(note.drop(to_delete))
        return ret
    
    # checks nearby notes for validation
    def filter_nearby_times(self, notes):
        self.start_offset = notes.iloc[0].time
        notes["time"]     = notes["time"] - self.start_offset
        notes["duration"] = notes.time.shift(-1) - notes.time
        notes["duration"] = notes.duration.map(closest_duration)
        notes["typ"]      = notes.duration.map(lambda x: duration_to_notes[x]["name"])
        return notes
    
    def format_notes(self, notes):
        measure_counter, time_counter = 0, 0
        curr_measure = Measure(measure_counter, self.time_signature[0], self.time_signature[1])
        for i in range(len(notes)):
            row = notes.iloc[i]
            note = Note(row.given_pitch, row.signal, row.loudness, row.time, duration=row.duration, typ=row.typ)
            if time_counter + row.duration > 4:
                # FIXME: this fills up the rest of the measure with a rest, but it can be better
                # Ideally it would be smart enough to wrap up a measure if there's little cutoff
                # or tie current note into next measure.
                curr_measure.wrap_up_time()
                self.addMeasure(curr_measure)
                measure_counter += 1
                time_counter = 0
                curr_measure = Measure(measure_counter, self.time_signature[0], self.time_signature[1])
            curr_measure.addNote(row)
        curr_measure.wrap_up_time()
        self.addMeasure(curr_measure)
            
        
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
