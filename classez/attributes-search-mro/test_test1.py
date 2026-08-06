import unittest

from test1 import A


class MyTest(unittest.TestCase):
    def test_some(self):
        a = A()
        self.assertEqual(a.flare, 46)

    def test_two(self):
        a = A()
        self.assertEqual(a.justice, 7778)


if __name__ == "__main__":
    unittest.main()
