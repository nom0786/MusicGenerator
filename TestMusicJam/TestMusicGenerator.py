import unittest
import sys
import os
sys.path.append("..") 
from MusicJam.music_generator import MusicGenerator
import music21
class TestMusicGenerator(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.ma1 = MusicGenerator([['C','G','B'],'1/2'],num_bars = 4,bpm=66)
        self.ma2 = MusicGenerator([['F','D','D#'],'1/1'],num_bars = 4,bpm=66)

    def test_rhythms(self):
        self.assertEqual(self.ma1.Key,'C')
        self.assertEqual(type(self.ma2.Beats),list)  
        self.assertEqual(type(self.ma1.ChordsPrg),list )  
        self.assertEqual(self.ma2.notelist_ipt,['F','D','D#'] )
    def test_func(self):
        self.assertEqual(type(self.ma1.chords_generate()[0]),music21.chord.Chord)
        self.assertEqual(type(self.ma1.mix_melody_chords()),music21.stream.base.Score)
        self.assertEqual(os.path.exists('../file.mid'),True)
        self.assertEqual(type(self.ma1.melody_generate()),list)

    @classmethod
    def tearDownClass(self):
        print("successful")
    


unittest.main(argv =[''], verbosity=2, exit=False)
