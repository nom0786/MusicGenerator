from music21 import *
import numpy as np
import random
class MusicGenerator:
    def __init__(self):
        self.chordPgsDgr = [
            ['I','IV','V','I'],['I','IV','V','V'],['I','IV','vi','V'],['I','V','vi','IV'],['I','V','vi','iii'],['I','vi','IV','V'],
            ['ii','V','I','I'],['ii','V','I','vi'],
            ['IV','I','IV','V'],
            ['vi','IV','I','V']]
        self.dgrKindMap = {
            'I':['','7','9','6'],
            'ii':['','7','9',''],
            'iii':['','7','9','sus2'], 
            'IV':['','7','9','sus4'],
            'V':['','7','9','sus2'],
            'vi':['','7','9','sus4'],
            'bVII':['']}
    def generateMusic(self):
        pc = stream.Stream()
        n_chordPg = len(self.chordPgsDgr)
        rd_chordPg_id = np.random.choice(n_chordPg)
        for i in range(4):
            chordPg = self.chordPgsDgr[rd_chordPg_id]
            if i == 3:
                kind = ''
            else:
                _kind = self.dgrKindMap[chordPg[i]]
                kind = random.choices(_kind,weights=(30,30,10,30))[0]
            chordDgrKind=chordPg[i]+kind
            print(chordDgrKind, end=' ') 
            for j in range(4):
                pc.append(roman.RomanNumeral(chordDgrKind))
        # pc.show('midi')
        pc.write('midi', fp='filename.mid')
