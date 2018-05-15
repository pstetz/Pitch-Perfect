NUM_OCTAVES = 6
UNQ_NOTES = 12

# [next_note_freq] / [curr_note_freq] = HALF_STEP_RATIO
HALF_STEP_RATIO = 1.059462742437609

class Music_Gen:
    def __init__(self, music_segment, curr_octave=3):
        self.curr_octave = curr_octave
        self.seg = music_segment
        del music_segment
        
        self._get_notes()
        self._clip_length()
        
    def ret(self):
        return self.segs
        
    def _change_speed(self, seg, freq):
        ret = list()
        x = 0
        while x + 1 < len(seg):
            i = int(x)
            start = seg[i]
            end = seg[i + 1]
            diff = end - start
            ret.append(start + (diff * (x % 1)))
            x += freq
        return ret

    def _get_octaves(self, seg):
        lower_num = self.curr_octave - 1
        higher_num = NUM_OCTAVES - self.curr_octave
        ret = list()
        for i in range(lower_num+1, 1, -1):
            speed = 0.5**i
            ret.append(self._change_speed(seg, speed))
        ret.append(self.seg)
        for i in range(1, higher_num+1):
            speed = 2**i
            ret.append( self._change_speed(seg, speed) )
        return ret

    def _clip_length(self):
        min_length = min([len(seg) for seg in self.segs])
        self.segs = [seg[:min_length] for seg in self.segs]

    def _get_notes(self):
        notes = list()
        for i in range(UNQ_NOTES):
            speed = HALF_STEP_RATIO ** i
            curr = self._change_speed(self.seg, speed)
            notes.append(self._get_octaves(curr))

        ret = list()
        for i in range(NUM_OCTAVES):
            for j in range(UNQ_NOTES):
                ret.append(notes[j][i])
        self.segs = ret
        