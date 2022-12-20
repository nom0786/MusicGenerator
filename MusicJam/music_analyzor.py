from music21 import *
import numpy as np
import random

class MusicAnalyzor:
    def __init__(self, note_object, num_bars=4, bpm=75):
        self.note_num = {
            '0':['C'], '1':['C#','Db'], '2':['D'], '3':['D#','Eb'], '4':['E'],
            '5':['F'], '6':['F#','Gb'],
            '7':['G'], '8':['G#','Ab'], '9':['A'], '10':['A#','Bb'], '11':['B']
        } # the relationship between number and notes
        self.keys_character = {
            '0':['0','2','4','5','7','9','11'],
            '1':['0','1','3','5','6','8','10'],
            '2':['1','2','4','6','7','9','11'],
            '3':['0','2','3','5','7','8','10'],
            '4':['1','3','4','6','8','9','11'],
            '5':['0','2','4','5','7','9','10'],
            '6':['1','3','5','6','8','10','11'],
            '7':['0','2','4','6','7','9','11'],
            '8':['0','1','3','5','7','8','10'],
            '9':['1','2','4','6','8','9','11'],
            '10':['0','2','3','5','7','9','10'],
            '11':['1','3','4','6','8','10','11']
        } # all the notes_nums of key_nums
        self.rhythms = ['1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','0','1110','1101','1011','1010','0111','0101']
        self.notelist_ipt = note_object[0]
        print("{0}Input:{1} {2}{3}{4}".format('\033[1m','\033[0m','\033[0:35m',str(note_object),'\033[0m'))
        self.rhythm_ipt = note_object[1]
        self.meter = '4/4'
        self.chordPgsDgr = [
            ['I','IV','V','I'],['I','IV','V','V'],['I','IV','vi','V'],['I','V','vi','IV'],['I','V','vi','iii'],['I','vi','IV','V'],
            ['ii','V','I','I'],['ii','V','I','vi'],['ii','vi','I','iii'],
            ['IV','I','IV','V'],['IV','V','I','vi'],['IV','II','V','I'],
            ['vi','IV','I','V'],['vi','I','II','V'],['vi','I','IV','V']
            ]
        self.dgrKindMap = {
            'I':['','7','9','6'],
            'ii':['','7','9',''],
            'iii':['','7','9','sus2'], 
            'IV':['','7','9','sus2'],
            'V':['','','9','sus2'],
            'vi':['','7','9','sus4'],
            'bVII':['']
            }
        self.num_bars= num_bars
        self.bpm = bpm

    def key_analyze(self):
        '''Transfer notes to note_nums'''
        notelist_num = []
        for note in self.notelist_ipt:
            for num in self.note_num:
                if note in self.note_num[num]:
                    notelist_num.append(num)
        count_note_ipt = {}
        # Count the number of characteristic notes of different input notes for each keys
        for keynum in self.keys_character:
            i = 0
            for notenum in notelist_num:
                if notenum in self.keys_character[keynum]:
                    i += 1
            count_note_ipt[keynum]=i
        return count_note_ipt

    def rhythm_analyze(self):
        '''Determine the rhythm of the first bar.'''
        _rhythmmap={
            '1/2':['1101',['11','10']],
            '1/1':['1110','0111',['11','10'],['11','11'],['01','11']],
            '2/1':['1011',['10','11']]
            }
        rhythm_start = random.choices(_rhythmmap[self.rhythm_ipt])
        if isinstance(rhythm_start[0],list):
            rhythm_start=rhythm_start[0]
        return rhythm_start
        
    def key_setting(self):
        '''Set the key fron the analyzing result of key_analyze.'''
        count_note_ipt = self.key_analyze()
        # find the largest frequency of each keys, if multiple then randomly choose one.
        maxfreq_character_notes = max(list(count_note_ipt.values()))
        _freq_Keys = [k for k, v in count_note_ipt.items() if v == maxfreq_character_notes][0] # get the list of keys which have max frequency of input notes.
        Key = self.note_num[random.choice(_freq_Keys)][-1] 
        return Key

    def rhythm_setting(self):
        '''Use the rhythm_start to generate self.num_bars bars of beats.'''
        rhythm_start = self.rhythm_analyze()
        rtm_beats = rhythm_start
        # rtm_beats.extend(rhythm_start)
        for i in range(self.num_bars*4-len(rtm_beats)):
            rtm_beats.append(random.choices(self.rhythms)[0])
        return rtm_beats

    def chords_setting(self):
        '''Chords Progression Setting'''
        n_chordPg = len(self.chordPgsDgr)
        rd_chordPg_id = np.random.choice(n_chordPg)
        chords_lst = []
        for i in range(4):
            chordPg = self.chordPgsDgr[rd_chordPg_id]
            if i == 3:
                kind = '' # the last chord should be terminating harmony.
            else:
                _kind = self.dgrKindMap[chordPg[i]]
                kind = random.choices(_kind,weights=(30,30,10,30))[0] # Randomly choose a chord progression with some probility distribution.
            chordDgrKind=chordPg[i]+kind # add the terminating harmony.
            chords_lst.append(chordDgrKind)
        return chords_lst