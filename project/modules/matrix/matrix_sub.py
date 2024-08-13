from bottle import route, run, request
import json
import numpy as np

@route('/generate', method='POST')
def generate():
    matrix1 = json.loads(request.forms.get('matrix1'))
    matrix2 = json.loads(request.forms.get('matrix2'))
    # Perform operations...
    result = elementWiseSubtraction(matrix1, matrix2)
    return json.dumps(result)

@route('/subtract', method='POST')
def subtract():
    matrix1 = json.loads(request.forms.get('matrix1'))
    matrix2 = json.loads(request.forms.get('matrix2'))
    # Perform operations...
    result = calculateDiffMatrix(matrix1, matrix2)
    return json.dumps(result)

def matrixToString(matrix):
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])

def elementWiseSubtraction(matrix1, matrix2):
    np_matrix1 = np.array(matrix1)
    np_matrix2 = np.array(matrix2)
    result = np_matrix1 - np_matrix2
    return result.tolist()

def calculateDiffMatrix(matrix1, matrix2):
    np_matrix1 = np.array(matrix1)
    np_matrix2 = np.array(matrix2)
    result = np.abs(np_matrix1 - np_matrix2)
    return result.tolist()

run(host='localhost', port=8080)