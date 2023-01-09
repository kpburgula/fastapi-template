import unittest
import requests
from config.config import *
  
class SampleTestCase(unittest.TestCase):
  
    # sample test case 1
    def test_1(self):        
        self.assertTrue(requests.get(URL_1).status_code == 200)
    
    # sample test case 2
    def test_2(self):        
        self.assertTrue(requests.get(URL_2).status_code == 200)
    
    # sample test case 3
    def test_3(self):        
        self.assertTrue(requests.get(URL_2).json()['Value'] == "This is a test and the value entered is 007")
  
if __name__ == '__main__':
    unittest.main()