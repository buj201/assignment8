'''
Created on Nov 5, 2015

@author: ds-ga-1007
'''
import unittest
from simulate_bets import *

class Test(unittest.TestCase):


    def test_get_bets_from_positions(self):
        self.assertEqual(get_bets_from_positions([1]).shape, (1,1))
        self.assertEqual(get_bets_from_positions([1,10]).shape, (10,2))
        self.assertEqual(get_bets_from_positions([10,100,1000]).shape, (1000,3))
    
    def test_get_cumu_return_for_day(self):
        self.assertEqual(get_cumu_return_for_day([1,10,100]).shape, np.array([1,10,100]).shape)
    
    def test_get_daily_returns_for_n_days(self):
        self.assertEqual(get_daily_returns_for_n_days([1,10,100,1000],37).shape, (37,4))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()