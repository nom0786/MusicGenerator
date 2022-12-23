import unittest
from TestMusicPlayer.test_interface import TestInterface
from TestMusicPlayer.test_notes import TestNotes
from TestMusicJam.TestMusicAnalyzor import TestMusicAnalyzor
from TestMusicJam.TestMusicGenerator import TestMusicGenerator

def TestSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNotes))
    # suite.addTest(unittest.makeSuite(TestInterface))
    suite.addTest(unittest.makeSuite(TestMusicAnalyzor))
    suite.addTest(unittest.makeSuite(TestMusicGenerator))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
TestSuite()