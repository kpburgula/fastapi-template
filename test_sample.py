import unittest
  
class SampleTestCase(unittest.TestCase):
  
    # sample test case 1
    def test_1(self):        
        self.assertTrue(200 == 200)
    
    
    # sample test case 2
    def test_2(self):        
        self.assertTrue("Test" == "Test")
  
if __name__ == '__main__':
    unittest.main()