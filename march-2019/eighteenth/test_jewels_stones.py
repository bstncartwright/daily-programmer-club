from jewels_stones import num_jewels_and_stones    # The code to test
import unittest   # The test framework


class Test_TestJewelsAndStones(unittest.TestCase):
    def test_case_one(self):
        # arrange
        expected = 3
        # act
        result = num_jewels_and_stones('aA', "aAAbbbb")
        # assert
        self.assertEqual(result, expected)

    def test_case_two(self):
        expected = 0
        result = num_jewels_and_stones("z", "ZZ")
        self.assertEqual(result, expected)

    def test_case_three(self):
        expected = 7
        result = num_jewels_and_stones("zz", "zzzzzzz")
        self.assertEqual(result, expected)
    
    def test_case_four(self):
        expected = 8
        result = num_jewels_and_stones("abcdef", "bbbcccffuu")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
