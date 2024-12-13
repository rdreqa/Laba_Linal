import unittest
from Task_1 import *


class Test_CSR_matrix(unittest.TestCase):
    def setUp(self):
        self.matrix_sq = CSR_Func([
            [1, 2, 3, 0],
            [6, 8, 3, 1],
            [80, 3, 3, 4],
            [2, 11, 4, 5]
        ])
        self.matrix_not_sq = CSR_Func([
            [1, 8, 4],
            [0, 7, 0]
        ])
        self.matrix_5x5 = CSR_Func([
            [9, 0, 5, 3, 3],
            [0, 0, 0, 7, 6],
            [4, 0, 8, 0, 8],
            [0, 0, 0, 3, 2],
            [0, 1, 0, 6, 0]
        ])
        self.zero_matrix = CSR_Func([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
    def test_trace(self):
        self.assertEqual(self.matrix_sq.trace(), 17)
        self.assertEqual(self.matrix_5x5.trace(), 20)
        self.assertEqual(self.zero_matrix.trace(), 0)
        with self.assertRaises(AssertionError):
            self.matrix_not_sq.trace()

    def test_get_element(self):

        self.assertEqual(self.matrix_sq.get_element(1, 1), 1)
        self.assertEqual(self.matrix_sq.get_element(3, 1), 80)
        self.assertEqual(self.matrix_not_sq.get_element(2, 2), 7)

        self.assertEqual(self.zero_matrix.get_element(1, 1), 0)

        with self.assertRaises(AssertionError):
            self.matrix_not_sq.get_element(4, 4)

if __name__ == "__main__":
    unittest.main()
