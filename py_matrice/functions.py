def transpose(matrix):
	for i in range(len(matrix)):
		for j in range(i, len(matrix[0])):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix

def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	if len(matrix) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	det = 0
	for i in range(len(matrix)):
		sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
		det += matrix[0][i] * determinant(sub_matrix) * (-1) ** i
	return det