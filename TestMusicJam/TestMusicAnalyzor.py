import unittest
import sys
sys.path.append("..") 
from MusicJam.music_analyzor import MusicAnalyzor 
class TestMusicAnalyzor(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.ma1 = MusicAnalyzor([['C','G','B'],'1/2'],num_bars = 4,bpm=66)
        self.ma2 = MusicAnalyzor([['F','D','D#'],'1/1'],num_bars = 4)
    def test_rhythms(self):
        self.assertEqual(self.ma1.rhythms,['1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','0','1110','1101','1011','1010','0111','0101'])
        self.assertEqual(self.ma2.rhythms,['1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','1','01','11','1111','0','1110','1101','1011','1010','0111','0101'])  
        self.assertEqual(self.ma1.rhythm_ipt,'1/2' )  
        self.assertEqual(self.ma2.notelist_ipt,['F','D','D#'] )
    def test_key_analyze(self):
        self.assertEqual(type(self.ma1.key_analyze()),dict)
        self.assertEqual(len(self.ma1.key_analyze()),len(self.ma1.keys_character))
        self.assertEqual(self.ma1.key_setting(),'C')
        self.assertEqual(type(self.ma1.rhythm_setting()),type(self.ma2.chords_setting()))

    @classmethod
    def tearDownClass(self):
        print("successful")


unittest.main(argv =[''], verbosity=2, exit=False)
