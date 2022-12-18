import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
sys.path.append(parent)

from MusicPlayer.interface import MusicInterface as m

class TestInterface(unittest.TestCase):

    def check_notes_status(self): 
        self.assertEqual(m.initialize_interface())



unittest.main(argv=[''], verbosity=2, exit=False)
