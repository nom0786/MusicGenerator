import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
sys.path.append(parent)

from MusicPlayer.interface import *

class TestInterface(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.m1 = MusicInterface

    def test_check_notes_status(self): 
        self.assertEqual(self.m1.check_notes_status(['A', 'B', 'C']), True)
        self.assertEqual(self.m1.check_notes_status(['C', 'C']), False)
        self.assertEqual(self.m1.check_notes_status(['B', 'E', 'D']), True)
        self.assertEqual(self.m1.check_notes_status([]), False)

unittest.main(argv=[''], verbosity=2, exit=False)