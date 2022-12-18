import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
sys.path.append(parent)

from MusicPlayer.notes import notes as n

class TestNotes(unittest.TestCase):

    def test_calculate_duration(self): 
        self.assertEqual(n.calculate_duration(self, [2,4,8]), 0.5)

    def test_calculate_speed(self): 
        self.assertEqual(n.calculate_speed(self, [1,5,10]), 9)

    def test_convert_duration(self): 
        self.assertEqual(n.convert_duration(self, 0.5), '1/2')
        self.assertEqual(n.convert_duration(self, 1), '1/1')
        self.assertEqual(n.convert_duration(self, 2), '2/1')      

    def test_convert_duration(self): 
        self.assertEqual(n.convert_duration(self, 0.5), '1/2')
        self.assertEqual(n.convert_duration(self, 1), '1/1')
        self.assertEqual(n.convert_duration(self, 2), '2/1')



unittest.main(argv=[''], verbosity=2, exit=False)
