import unittest
from Task_3 import *
class Test_determinant(unittest.TestCase):
    def setUp(self):
        self.matrix_sq = CSR_Func([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
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
        self.matrix_2x2 = CSR_Func([
            [4, 3],
            [6, 3]
        ])
        self.matrix_negativ_values = CSR_Func([
            [-2, 2, -3],
            [-1, -1, -3],
            [-2, 0, -1]
        ])

    def test_determinant(self):
        self.assertEqual(determinant_func(self.matrix_2x2), -6.0)
        self.assertEqual(determinant_func(self.matrix_sq), 0.0)
        self.assertEqual(determinant_func(self.matrix_5x5), -208.0)
        self.assertEqual(determinant_func(self.zero_matrix), 0.0)
        self.assertEqual(determinant_func(self.matrix_negativ_values), 14.0)

        with self.assertRaises(AssertionError):
            determinant_func(self.matrix_not_sq)

if __name__ == "__main__":
    unittest.main()
