import unittest
from TestClasses.test_interface import *
from TestClasses.test_notes import TestNotes

def TestSuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestNotes))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    # print(result)
    
TestSuite()