import unittest
class IdentityTests(unittest.TestCase):
    def test_identicality(self):
        a=[1,2,3]
        b=a
        c=[1,2,3]
        
        self.assertEqual(a,b)
        self.assertEqual(a,c)
        
        self.assertIs(a,b)
        # a and c are equal but not identical.
        self.assertIsNot(a,c)
        
if __name__=="__main__":
    unittest.main()