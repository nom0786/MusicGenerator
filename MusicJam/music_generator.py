from MusicJam.music_analyzor import *
from music21 import *
import time
import os

# color refer: https://xdevs.com/guide/color_serial/

class MusicGenerator(MusicAnalyzor):
    def __init__(self, note_object,num_bars,bpm):
        MusicAnalyzor.__init__(self, note_object, num_bars,bpm)
        # self.Key = self.key_setting()
        self.Key = "C"
        tm1 = time.time()
        print("{0}rhythm beats{1}: start generating...".format('\033[1m','\033[0m'),end="")
        self.Beats = self.rhythm_setting()
        tm2 = time.time()
        print("{1}s...finished generating\n {2}{3}{4}".format('',str(round(tm2-tm1,5)),'\033[93m',str(self.Beats),'\033[0m'))
        tm1 = time.time()
        print("{0}chords progression:{1} start generating...".format('\033[1m','\033[0m'),end="")
        self.ChordsPrg = self.chords_setting()
        tm2 = time.time()
        print("{1}s...finished generating\n {2}{3}{4}".format('',str(round(tm2-tm1,5)),'\033[92m',str(self.ChordsPrg),'\033[0m'))

    def chords_generate(self):
        chords_lst=[]
        for j in range(4): #four 
            for i in range(2):
                _chord = roman.RomanNumeral(self.ChordsPrg[j])
                _chord= " ".join([str(p) for p in _chord.pitches])
                # change from RomanNumeral to origin chords
                crd = chord.Chord(_chord)
                crd.key = self.Key
                crd.duration.type = 'half'
                chords_lst.append(crd)
        return chords_lst

    def melody_generate(self):
        '''generate melody_notes list based on key, chord progression and beats.'''
        cnt_notes_bar = [len(x) for x in self.Beats]
        _melody_notes = []
        for num_beat in range(len(self.Beats)):
            num_chord = num_beat//len(self.ChordsPrg)
            rf = roman.RomanNumeral(self.ChordsPrg[num_chord], self.Key) # transfer roman numerals to chords based on key.
            chordNotes = rf.normalOrder # get the pitches of chords
            _melody_notes.append(random.choices(chordNotes,k=cnt_notes_bar[num_beat])) # randomly generate notes based on chords.
        melody_lst=self.melody_str2notes(_melody_notes)
        melody_lst=self.melody_f3notes(melody_lst)
        return melody_lst

    def melody_str2notes(self,_melody_notes):
        melody_lst = []
        # Fill notes to beats
        for num_melody in range(len(_melody_notes)):  
            itm= _melody_notes[num_melody]
            # type of the note beat
            if len(itm) == 4: _type = '16th' # Sixteenth note type
            elif len(itm) == 2: _type = 'eighth' # Eighth note type
            elif len(itm) == 1: _type = 'quarter' # Quarter note type
            for num_itm in range(len(itm)):
                itm_melody = itm[num_itm]
                # combine to note.Note
                if self.Beats[num_melody][num_itm] == '0':
                    _note = note.Rest(type = _type) # Rest note
                else:
                    _note = note.Note(self.note_num[str(itm_melody)][0], type = _type) # Pitch note
                melody_lst.append(_note)
        return melody_lst

    def melody_f3notes(self,melody_lst):
        f3idx = []
        for num_mld_note in range(len(melody_lst)):
            if melody_lst[num_mld_note].isNote:
                f3idx.append(num_mld_note) 
                if len(f3idx)>= len(self.notelist_ipt):
                    break
        for _num_idx in range(len(f3idx)):
            melody_lst[f3idx[_num_idx]] = note.Note(self.notelist_ipt[_num_idx],type = melody_lst[f3idx[_num_idx]].duration.type)
        return melody_lst

    def mix_melody_chords(self):
        s = stream.Score()
        mm1 = tempo.MetronomeMark(number=self.bpm)
        # create melody part of the score
        p_melody = stream.Part()
        p_melody.append(mm1)

        # generate chords
        tm1 = time.time()
        print("{0}chord:{1} start generating...".format('\033[1m','\033[0m'),end="")
        chords_lst = self.chords_generate() # generate chords
        tm2 = time.time()
        print("{1}s...finished generating\n{2} {3}{4} ".format('',str(round(tm2-tm1,5)),'\033[94m',str(chords_lst),'\033[0m'))

        # generate melody
        tm1 = time.time()
        print("{0}melody:{1} start generating...".format('\033[1m','\033[0m'),end="")
        melody_lst = self.melody_generate() 
        tm2 = time.time()
        print("{1}s...finished generating\n{2} {3}{4} ".format('',str(round(tm2-tm1,5)),'\033[94m',str(melody_lst),'\033[0m'))

        # mixtion
        tm1 = time.time()
        print("{0}mixtion{1}: melody and chords start mixing...".format('\033[1m','\033[0m'),end="")
        for note in melody_lst:
            p_melody.append(note)
        
        # create chords part of the score
        p_chords = stream.Part()
        p_chords.append(mm1)
        for num_chord in range(len(chords_lst)):
            p_chords.insert(num_chord*2, chords_lst[num_chord])
        
        # mix the melody and chords
        s.insert(0,p_melody)
        s.insert(0,p_chords)
        tm2 = time.time()
        print("{0}s...finished mixing".format(str(round(tm2-tm1,5))))
        
        # write outputs
        tm1 = time.time()
        print("{0}outputs:{1} start writing...".format('\033[1m','\033[0m'),end="")
        fp_output = ['file.mid','score-1.png','score.musicxml']
        for fp in fp_output:
            if os.path.exists(fp):
                os.remove(fp)
            s.write('midi', fp='file.mid')
        tm2 = time.time()
        print("{2}s...{0}midi{1} finished writing...".format('\033[1m','\033[0m',str(round(tm2-tm1,5))),end='')
        s.write('musicxml.png',fp = 'score.png')
        tm3 = time.time()
        print("{0}s...{1}png {2} finished writing ".format(str(round(tm3-tm1,5)),'\033[1m','\033[0m'))
        
        return s