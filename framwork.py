import unittest

class UnitTest(unittest.TestCase):
    def test_sample(self):
        a = 10
        b = 20
        #Positive
        self.assertEqual(a,b, msg=" 10 is NOT Equal to 20")

        # Nagative
        #self.assertNotEqual(a, b, msg=" 10 is NOT Equal to 20")

if __name__ == "__main__":
    unittest.main()
