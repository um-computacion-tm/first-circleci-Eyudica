import unittest
from main import functionci

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(functionci(1,2),3)

if __name__ == '__main__':
    unittest.main()
