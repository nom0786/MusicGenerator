import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
sys.path.append(parent)


from MusicPlayer.notes import notes as n

class TestNotes(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.n1 = n()
        self.n2 = n()
        self.n3 = n()
        self.n4 = n()
        self.n5 = n()
        self.n6 = n()

        self.n3.notes = ['A', 'B', 'C']
        self.n3.times = [2, 4, 8]

        self.n4.notes = ['E', 'C', 'C']
        self.n4.times = [1, 15, 18]

        self.n5.notes = ['D', 'E', 'F']
        self.n5.times = [1, 3, 5]

        self.n6.notes = ['B', 'B', 'B']
        self.n6.times = [0, 2, 4]

    def test_calculate_duration(self): 
        self.assertEqual(self.n1.calculate_duration([2,4,8]), 0.5)
        self.assertEqual(self.n2.calculate_duration([1, 15, 18]), 2)  
        self.assertEqual(self.n1.calculate_duration([1, 3, 5]), 1) 
        self.assertEqual(self.n1.calculate_duration([4, 6, 10]), 0.5)        
        
    def test_calculate_speed(self): 
        self.assertEqual(self.n1.calculate_speed([1,5,10]), 9)
        self.assertEqual(self.n2.calculate_speed([3, 5, 7]),4)
        self.assertEqual(self.n1.calculate_speed([0, 1, 2]), 2)
        self.assertEqual(self.n2.calculate_speed([4, 7, 22]), 18)

    def test_convert_duration(self): 
        self.assertEqual(self.n1.convert_duration(0.5), '1/2')
        self.assertEqual(self.n2.convert_duration(2), '2/1')
        self.assertEqual(self.n1.convert_duration(1), '1/1')
        self.assertEqual(self.n2.convert_duration(10), '2/1')  

    def test_export_notes(self): 
        self.assertEqual(self.n3.export_notes(), [['A', 'B', 'C'], '1/2', 6])
        self.assertEqual(self.n4.export_notes(), [['E', 'C', 'C'], '2/1', 17])
        self.assertEqual(self.n5.export_notes(), [['D', 'E', 'F'], '1/1', 4])
        self.assertEqual(self.n6.export_notes(), [['B', 'B', 'B'], '1/1', 4])


    @classmethod
    def tearDownClass(self):
        print("successful")

unittest.main(argv=[''], verbosity=2, exit=False)
