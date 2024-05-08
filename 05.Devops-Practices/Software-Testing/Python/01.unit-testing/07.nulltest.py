import unittest
def explicit_return_sum(a,b):
    return a+b
def implicit_return_sum(a,b):
    print(a+b)

class TestNone(unittest.TestCase):
    def test_sum_functions(self):
        self.assertIsNone(implicit_return_sum(3,5))
        self.assertIsNotNone(explicit_return_sum(10,2))


if __name__=="__main__":
    unittest.main()