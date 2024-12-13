import unittest
from Task_2 import *
from Task_1 import *


class Test_operations_with_matrix(unittest.TestCase):
    def setUp(self):
        self.matrix_sq = CSR_Func([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.matrix_5x5 = CSR_Func([
            [9, 0, 5, 3, 3],
            [0, 0, 0, 7, 6],
            [4, 0, 8, 0, 8],
            [0, 0, 0, 3, 2],
            [0, 1, 0, 6, 0]
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



    def test_Sum_matrices(self):
        """Тест сложения двух матриц"""

        result = sum_matrix(self.matrix_sq,self.matrix_negativ_values)

        expected_values = [-1, 4, 3, 4, 3, 5, 8, 8]
        expected_cols = [0, 1, 0, 1, 2, 0, 1, 2]
        expected_rows = [1, 3, 6, 9]

        self.assertEqual(result.important_values, expected_values)
        self.assertEqual(result.col, expected_cols)
        self.assertEqual(result.rows, expected_rows)

        with self.assertRaises(ValueError):
            sum_matrix(self.matrix_5x5, self.matrix_2x2)

    def test_multiply_scalar(self):
        """Тест умножения матрицы на скаляр"""

        scalar = 2
        result = Multi_scalaris(scalar, self.matrix_negativ_values)

        expected_values = [-4, 4, -6, -2, -2, -6, -4, -2]
        expected_cols = [0, 1, 2, 0, 1, 2, 0, 2]
        expected_rows = [1, 4, 7, 9]

        scalar_2 = 0
        result_2= Multi_scalaris(scalar_2, self.matrix_negativ_values)
        expected_values_2 = []
        expected_cols_2 = []
        expected_rows_2 = [1] * self.matrix_negativ_values.M + [1]



        self.assertEqual(result.important_values, expected_values)
        self.assertEqual(result.col, expected_cols)
        self.assertEqual(result.rows, expected_rows)
        self.assertEqual(result_2.important_values, expected_values_2)
        self.assertEqual(result_2.col, expected_cols_2)
        self.assertEqual(result_2.rows, expected_rows_2)

    def test_multiply_matrices(self):
        """Тест умножения двух матриц"""


        result = Multi_matrix(self.matrix_sq, self.matrix_negativ_values)

        expected_values = [-10, -12, -25, 3, -33, -40, 6, -54]
        expected_cols = [0, 2, 0, 1, 2, 0, 1, 2]
        expected_rows = [1, 3, 6, 9]

        self.assertEqual(result.important_values, expected_values)
        self.assertEqual(result.col, expected_cols)
        self.assertEqual(result.rows, expected_rows)

        with self.assertRaises(ValueError):
            Multi_matrix(self.matrix_5x5, self.matrix_2x2)


if __name__ == '__main__':
    unittest.main()
