from valid_walk import is_valid_walk
import unittest
class Test_valid_walk(unittest.TestCase):
    def test_should_return_false_if_less_than_10_1(self):
        walk = ['n']
        self.assertFalse(is_valid_walk(walk))

    def test_should_return_false_if_less_than_10_2(self):
        walk = ['n', 's', 'e', 'w']
        self.assertFalse(is_valid_walk(walk))

    def test_should_return_false_if_greater_than_10_1(self):
        walk = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w',
                'n', 's', 'e', 'w', 'n', 's', 'e', 'w']
        self.assertFalse(is_valid_walk(walk))

    def test_should_return_false_if_greater_than_10_2(self):
        walk = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w',
                'n', 's', 'e', 'w', 'n', 's', 'e', 'w',
                'n', 's', 'e', 'w', 'n', 's', 'e', 'w',
                'n', 's', 'e', 'w', 'n', 's', 'e', 'w']
        self.assertFalse(is_valid_walk(walk))

    def test_should_return_false_if_doesnt_return_1(self):
        walk = ['n', 's', 'n', 'n', 'w', 'w', 'e', 'n', 'w', 'n']
        self.assertFalse(is_valid_walk(walk))
    
    def test_should_return_false_if_doesnt_return_2(self):
        walk = ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'n']
        self.assertFalse(is_valid_walk(walk))

    def test_should_return_true_if_valid_walk_1(self):
        walk = ['n', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'w', 'w']
        self.assertTrue(is_valid_walk(walk))
    
    def test_should_return_true_if_valid_walk_2(self):
        walk = ['s', 'w', 'w', 'w', 'w', 'n', 'e', 'e', 'e', 'e']
        self.assertTrue(is_valid_walk(walk))


if __name__ == "__main__":
    unittest.main()
