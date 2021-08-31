import unittest


def sum(a, b):

    return a + b


class Sumtest(unittest.TestCase):
    def setUo(self):
        print("SetUp Called...")
        self.a = 10
        self.b = 20

    def test_sumfun_1(self):
        print("TEST -1 Called....")
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_sumfun_2(self):
        print("TEST -2 Called....")
        # Arrange
        a = 10
        b = 20

        # Act
        result = sum(b, a)

        # Assert
        self.assertEqual(result, b + a)


if __name__ == "__main__":
    unittest.main()
