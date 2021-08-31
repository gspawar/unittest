import unittest

def sum(a,b):
    return a+b

class Unit_test_1(unittest.TestCase):
    def test_fun_1(self):
        print("TEST -1 Called....")
        #Arrange
        a = 10
        b = 20

        #Act
        result = sum(a,b)

        #Assert
        self.assertEqual(result, a + b)

class Unit_test_2(unittest.TestCase):
    def test_fun_2(self):
        print("TEST -2 Called....")
        #Arrange
        a = 10
        b = 20

        #Act
        result = sum(b,a)

        #Assert
        self.assertEqual(result, b + a)


if __name__=="__main__" :
    unittest.main()
