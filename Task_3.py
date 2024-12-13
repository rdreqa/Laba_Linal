from Task_1 import *


def determinant_func(matrix):
    """
    Функция вычисления определителя матрицы
    :param matrix: Квадратная матрица
    """
    assert matrix.N == matrix.M, "Матрица должна быть квадратной."
    important_values, col, row, N, M = matrix.important_values,matrix.col,matrix.rows,matrix.N,matrix.M
    matrix = obratno(important_values,col,row,N,M)

    det = 1
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            found = False
            for k in range(i + 1, len(matrix)):
                if matrix[k][i] != 0:
                    found = True
                    if found:
                        matrix[i], matrix[k] = matrix[k], matrix[i]
                        det *= -1

            if found == False:
                return 0

        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                coeff = matrix[j][i] / matrix[i][i]
                for col in range(i, len(matrix)):
                    matrix[j][col] -= coeff * matrix[i][col]


    for i in range(len(matrix)):
        det *= matrix[i][i]

    return round(det,1)

def determinant():
    """
    Функция вычисляет определитель матрицы и выводит ответ на вопрос “Существует ли матрица, обратная данной?”
    """
    matrix = CSR()
    result = determinant_func(matrix)

    if result != 0:
        return 'да'
    else:
        return 'нет'
