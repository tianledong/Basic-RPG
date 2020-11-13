'''
CS 5001
Fall 2019
Homework #7
'''
import unittest
from unittest.mock import patch
from game import *

weight_dic = {'LAMP': 3, 'THUMB DRIVE': 0, 'ALGORITHMS BOOK': 2,
                  'HAIR CLIPPERS': 2, 'CARROT': 5, 'MOD_2': 0,
                  'DESK': 1000, 'FINAL EXAM': 1, 'KEY': 0,
                  'PROF KEITH': 1000, 'FRYING PAN': 3, 'LAPTOP': 1000,
                  'BOOKSHELF': 500}

class TestMove(unittest.TestCase):
    
    def test_int1(self):
        self.assertEqual(move([2, 0, 0, 0], 'N', 0), 1)
        self.assertEqual(move([3, 1, 0, 0], 'N', 1), 2)
        self.assertEqual(move([7, 0, 0, 0], 'N', 7), 6)
        self.assertEqual(move([0, 7, 10, 0], 'S', 8), 6)
    def test_int2(self):
        self.assertEqual(move([0, 7, 10, 0], 'W', 8), 8)
    def test_int3(self):
        self.assertEqual(move([-9, 8, 6, 0], 'N', 6), 6)
        
class TestCheck_item(unittest.TestCase):
    def test_print1(self):
        with patch('builtins.print') as mocked_print:
            check_item(['HAIR CLIPPERS'])
            mocked_print.assert_called_with('HAIR CLIPPERS')
    
    def test_print2(self):
        with patch('builtins.print') as mocked_print:
            check_item(['HAIR CLIPPERS', 'MOD_2'])
            mocked_print.assert_called_with('MOD_2')

class TestCheck_weight(unittest.TestCase):

    def test_true(self):
        self.assertTrue(check_weight(0, weight_dic, 'LAMP'))
        self.assertTrue(check_weight(8, weight_dic, 'HAIR CLIPPERS'))
        self.assertTrue(check_weight(7, weight_dic, 'FRYING PAN'))

    def test_false(self):
        self.assertFalse(check_weight(0, weight_dic, 'PROF KEITH'))
        self.assertFalse(check_weight(8, weight_dic, 'LAMP'))
        self.assertFalse(check_weight(5, weight_dic, 'LAPTOP'))
        
if __name__ == '__main__':
    unittest.main()
