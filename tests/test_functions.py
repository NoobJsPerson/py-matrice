from py_matrice import functions

def test_transpose():
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	transpoed_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
	assert functions.transpose(matrix) == transpoed_matrix