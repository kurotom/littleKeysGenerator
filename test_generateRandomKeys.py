from generateRandomKeys import main
import unittest

class TestGenerateRandomKeys(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(len(main()), 20)

if __name__ == '__main__':
    unittest.main()
