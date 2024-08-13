# modules/matrix.py
from bottle import Bottle, route, template, request, response

app = Bottle()

@app.route('/matrix')
def matrix():
    # Example data for the template
    data = {"message": "This is the matrix page."}
    return template('views/matrix/gauss_eli.html', data=data)

# Add other matrix-related routes here