class matrix_CSR:
    def __init__(self, important_values,col,rows,N,M):
        self.important_values = important_values
        self.col = col
        self.rows = rows
        self.N = N
        self.M = M

    def trace(self):
        """
        Метод для подсчета следа матрицы
        """
        assert self.N == self.M, "Матрица должна быть квадратной"
        sled = 0
        for i in range(self.M):
            sled+= matrix_CSR.get_element(self,i+1,i+1)
        return sled


    def get_element(self, row_index, col_index):
        """
        Метод для получения элемента по индексу строки и столбца.
        :param row_index: Индекс строки (начиная с 1)
        :param col_index: Индекс столбца (начиная с 1)
        """
        assert row_index-1 <= self.M and col_index-1 <= self.N, "Индексы должны быть корректными"

        count_values = self.rows[row_index] - self.rows[row_index-1]
        index_start = self.rows[row_index-1]-1
        for i in range(count_values):
            if self.col[index_start] == col_index-1:
                return self.important_values[index_start]
            index_start+=1
        return 0

def CSR_Func(matrix):
    """
   Функция для перевода матрицы в CSR форму.
   :param matrix: матрица в привычной форме
    """
    important_values = []
    col = []
    rows = [1]
    M = len(matrix)
    N = len(matrix[0])
    for i in range(M):
        current_element_in_row = 0
        for j in range(N):
            if matrix[i][j] != 0:
                important_values.append(matrix[i][j])
                col.append(j)
                current_element_in_row += 1
        rows.append(current_element_in_row + rows[i])
    return matrix_CSR(important_values,col,rows,N,M)

def CSR():
    """
   Ввод матрциы с клавиатуры и получение её в CSR форме.
    """
    print('Введите размерность матрицы')
    M, N = map(int, input().split())
    matrix = []
    print('Введите матрицу')
    for i in range(M):
        row = list(map(int, input().split()))
        if len(row) != N:
            raise ValueError("кол-во элементов не совпадает с нужным")
        matrix.append(row)
    return CSR_Func(matrix)

def obratno(important_values,col,row,N,M):
    """
       Функция перевода матрицы вида CSR в привычный вид.
       :param important_values: массив не нулевых элементов матрицы
       :param col: массив индексов столбоц соответствущих не нулевым элементам
       :param row: массив, в котором (i+1 элемент) - (i элемент) = количество не нулевых элементов в i-ой строке
    """
    matrix = [[0 for i in range(N)] for i in range(M)]
    for i in range(M):
        count = 0
        k = row[i]
        while count < row[i+1] - row[i]:
            matrix[i][col[k-1]] = important_values[k-1]
            count+=1
            k+=1
    return matrix


