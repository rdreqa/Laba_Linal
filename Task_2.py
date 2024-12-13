from Task_1 import matrix_CSR, CSR, CSR_Func, obratno

def sum_matrix(matrix_a, matrix_b):
    """
    Функция сложения двух матриц в формате CSR.
    :param matrix_a: Первая матрица (экземпляр matrix_CSR)
    :param matrix_b: Вторая матрица (экземпляр matrix_CSR)
    """
    if matrix_a.N != matrix_b.N or matrix_a.M != matrix_b.M:
        raise ValueError("Размерности матриц не совпадают.")

    col_result = []
    row_result = [1]
    important_values_result = []

    for i in range(matrix_b.M):
        rowa = {}
        rowb = {}
        k = 0
        count_a = matrix_a.rows[i + 1] - matrix_a.rows[i]
        count_b = matrix_b.rows[i + 1] - matrix_b.rows[i]
        la = matrix_a.rows[i] - 1
        lb = matrix_b.rows[i] - 1
        for o in range(count_a):
            rowa[matrix_a.col[la]] = matrix_a.important_values[la]
            la += 1
        for j in range(count_b):
            rowb[matrix_b.col[lb]] = matrix_b.important_values[lb]
            lb += 1
        for g in range(matrix_b.N):
            flag = False
            if g in rowa.keys():
                col_result.append(g)
                important_values_result.append(rowa[g])
                flag = True
                k += 1
            if g in rowb.keys():
                if flag == True and important_values_result[len(important_values_result) - 1] + rowb[g] == 0:
                    important_values_result.pop()
                    col_result.pop()
                    k-=1
                elif flag == True:
                    important_values_result[len(important_values_result) - 1] += rowb[g]
                else:
                    col_result.append(g)
                    important_values_result.append(rowb[g])
                    k += 1
        row_result.append(row_result[i] + k)
    return matrix_CSR(important_values_result, col_result, row_result, matrix_b.N, matrix_b.M)

def Multi_scalaris(scalar, matrix):
    """
    Функция умножение матрицы на скаляр.
    :param matrix: Матрица (экземпляр matrix_CSR)
    :param scalar: Число, на которое умножается матрица.
    """
    if scalar == 0:
        return matrix_CSR([], [], [1] * (matrix.M + 1), matrix.N, matrix.M)
    for i in range(len(matrix.important_values)):
        matrix.important_values[i] *= scalar
    return matrix

def Multi_matrix(matrix_a, matrix_b):
    """
    Функция Умножение двух матриц.
    :param matrix_a: первая матрица (экземпляр matrix_CSR)
    :param matrix_b: вторая матрица (экземпляр matrix_CSR)
    """
    if matrix_a.N != matrix_b.M:
        raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы.")

    current_row = []
    result_matrix = []
    important_values_A, col_A, row_A, N_A, M_A = matrix_a.important_values,matrix_a.col,matrix_a.rows \
    ,matrix_a.N,matrix_a.M
    important_values_B, col_B, row_B, N_B, M_B = matrix_b.important_values,matrix_b.col,matrix_b.rows\
        ,matrix_b.N,matrix_b.M

    matrix_A = obratno(important_values_A,col_A,row_A,N_A,M_A)
    matrix_B = obratno(important_values_B,col_B,row_B,N_B,M_B)
    for i in range(M_A):
        if len(current_row) > 0:
            result_matrix.append(current_row)
        current_row = []
        for j in range(N_B):
            g = 0
            current_element = 0
            while g < N_A:
                current_element += matrix_A[i][g] * matrix_B[g][j]
                g += 1
            current_row.append(current_element)
    result_matrix.append(current_row)
    return CSR_Func(result_matrix)


