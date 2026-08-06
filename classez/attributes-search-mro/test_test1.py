import unittest

from test1 import A


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.a = A()
    
    def test_one(self):
        self.assertEqual(self.a.flare, 46)

    def test_two(self):
        self.assertEqual(self.a.justice, 7778)

    def test_three(self):
        with self.assertRaises(ZeroDivisionError):
            1/0


if __name__ == "__main__":
    unittest.main()
