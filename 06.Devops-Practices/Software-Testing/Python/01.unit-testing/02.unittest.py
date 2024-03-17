import unittest
# let's test string methods using unit testing
class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"),["a","b","c"])
        self.assertEqual("d+e+f".split("+"),["d","e","f"])
    def test_count(self):
        self.assertEqual("beautiful".count("u"),2)
if __name__=="__main__":
    unittest.main()

