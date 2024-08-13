from sympy import symbols, simplify, sympify

def add_matrix(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    """
    # Ensure both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    # Perform element-wise addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            # Parse the cell values as SymPy symbols or numbers
            cell1 = sympify(matrix1[i][j])
            cell2 = sympify(matrix2[i][j])
            
            # Add the cell values
            result[i][j] = simplify(cell1 + cell2)
    
    return result

def matrix_to_string(matrix):
    """
    Converts a matrix to an array of LaTeX-formatted strings.
    """
    matrix_string = []
    for row in matrix:
        matrix_string.append(" & ".join(str(element) for element in row))
    return matrix_string

def element_wise_addition(matrix1, matrix2):
    """
    Performs element-wise addition of two matrices.
    """
    # Ensure both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for element-wise addition.")
    
    # Initialize the result matrix with the addition strings
    result = [[f"{matrix1[i][j]} + {matrix2[i][j]}" for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    
    return result