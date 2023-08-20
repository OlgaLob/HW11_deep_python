# 2. Создайте класс Матрица. Добавьте методы для:
# - вывода на печать
# - сравнения
# - сложения
# - умножения матриц


class Matrix:
    """Класс для создания матриц и операциями + и * над ними"""

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __eq__(self, other: object) -> bool:
        """Cравнение 2 матриц между собой, равны, если строки\столбцы двух матриц содержат одинаковое
        количество элементов"""

        if len(self.matrix) != len(other.matrix):
            return False
        else:
            __flag = False
            for i in range(len(self.matrix)):
                if self.matrix[i] == other.matrix[i]:
                    __flag = True
                else:
                    self._flag = False
            return __flag

    def __add__(self, other):
        """Сложение матриц"""

        if len(self.matrix) != len(other.matrix):
            raise ArithmeticError('Сложение матриц разной размерности не поддерживается!')
        else:
            result_matrix = []
            for i in range(len(self.matrix)):
                line1 = self.matrix[i]
                line2 = other.matrix[i]
                c = [x + y for x, y in zip(line1, line2)]
                result_matrix.append(c)
            return Matrix(result_matrix)

    def __mul__(self, other):
        """Умножение матриц"""

        if len(self.matrix[0]) != len(other.matrix):
            raise ArithmeticError('Умножение матриц разной размерности не поддерживается!')
        else:
            result = []
            for i in range(len(self.matrix)):
                new_row = []
                for j in range(len(other.matrix[0])):
                    elem = 0
                    for k in range(len(other.matrix)):
                        elem += self.matrix[i][k] * other.matrix[k][j]
                    new_row.append(elem)
                result.append(new_row)
            return Matrix(result)

    def __str__(self) -> str:
        result_string = ''

        for i in self.matrix:
            result_string += f'{i}\n'

        return result_string


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[10, 2, 3], [40, 5, 6], [7, 8, 90]])
matrix_4 = Matrix([[10, 2, 3], [40, 5, 6]])

print(matrix_1 == matrix_2)
print(matrix_3 == matrix_4)

print(matrix_1 + matrix_3)

print(matrix_1 * matrix_3)

# Контроль размерности
print(matrix_1 * matrix_4)
print(matrix_1 + matrix_4)
