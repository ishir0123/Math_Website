from bottle import Bottle, run, template, static_file, error, request, response
import os
import logging
from bottle_cors_plugin import cors_plugin
import json
from modules import home, utils 
from modules.matrix import matrix, matrix_LU_dool, matrix_add
from modules.matrix.matrix_add import add_matrix, matrix_to_string,element_wise_addition # Import the new functions
from modules.matrix.matrix_sub import subtract, elementWiseSubtraction,calculateDiffMatrix # Import the subtraction function


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create the Bottle app
app = Bottle()
app.install(cors_plugin())

# Include routes from modules
app.merge(home.app)
app.merge(matrix.app)

# Define routes for other pages
@app.route('/integration')
def integration():
    # Example data for the template
    data = {"message": "This is the integration page."}
    return template('views/integration.html', data=data)

@app.route('/derivative')
def derivative():
    # Example data for the template
    data = {"message": "This is the derivative page."}
    return template('views/derivative.html', data=data)

@app.route('/about')
def about():
    return template('views/about.html')

@app.route('/matrix/<filename:path>')
def serve_matrix(filename):
    return static_file(filename, root='views/matrix')

@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='static')

# Route for serving static files
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

# Error handling
@app.error(404)
def error404(error):
    logging.error(f"404 Error: {error}")
    return template('views/404.html', error=error)

# New route for adding matrices
@app.route('/add_matrices', method='POST')
def add_matrices_route():
    try:
        data = request.json
        matrix1 = data.get('matrix1')
        matrix2 = data.get('matrix2')

        logging.info(f"Received matrices: {matrix1} and {matrix2}")

        if not matrix1 or not matrix2:
            response.status = 400
            return json.dumps({"error": "Matrices not provided"})

        matrix_a_string = f"A = {matrix_to_string(matrix1)}"
        matrix_b_string = f"B = {matrix_to_string(matrix2)}"
        matrix_addition_string = f"A + B = {matrix_to_string(matrix1)} + {matrix_to_string(matrix2)}"
        element_wise_matrix = element_wise_addition(matrix1, matrix2)
        element_wise_string = matrix_to_string(element_wise_matrix)
        result = add_matrix(matrix1, matrix2)
        result_string = f"A + B = {matrix_to_string(result)}"
        
        # Return the steps as a response
        return json.dumps({
            'step1': matrix_a_string,
            'step2': matrix_b_string,
            'step3': matrix_addition_string,
            'step4': element_wise_string,  # Use the result of the element-wise addition for step 4
            'step5': result_string
        })
    except Exception as e:
        logging.error(f"Error adding matrices: {e}")
        response.status = 500
        return json.dumps({"error": str(e)})

# New route for subtracting matrices
@app.route('/sub_matrix', method='POST')
def sub_matrix_route():
    data = request.json
    matrix1 = data.get('matrix1')
    matrix2 = data.get('matrix2')

    logging.info(f"Received matrices: {matrix1} and {matrix2}")

    if not matrix1 or not matrix2:
        response.status = 400
        return json.dumps({"error": "Matrices not provided"})

    # Calculate the element-wise subtraction matrix
    diff_matrix = calculate_diff_matrix(matrix1, matrix2)
    # Calculate the final result
    result =subtract(matrix1, matrix2)

    # Convert all matrices to string representations
    matrix1_string = matrix_to_string(matrix1)
    matrix2_string = matrix_to_string(matrix2)
    diff_matrix_string = matrix_to_string(diff_matrix)
    result_string = matrix_to_string(result)

    return json.dumps({
        "matrix1": matrix1_string,
        "matrix2": matrix2_string,
        "element_wise_subtraction": diff_matrix_string,
        "result": result_string
    })
# Run the app
if __name__ == "__main__":
    run(app, host='localhost', port=5000, debug=True)