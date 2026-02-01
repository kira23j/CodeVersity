import unittest
class TruthinessAndFalsinessTest(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(3<5)
        self.assertTrue(1)
        self.assertTrue("hello")
        self.assertTrue(["a"])
        self.assertTrue({"b":5})
    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse([])
        self.assertFalse({})
if __name__=="__main__":
    unittest.main()