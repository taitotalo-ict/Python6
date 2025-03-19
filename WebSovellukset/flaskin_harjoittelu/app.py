from flask import (
    Flask, 
    url_for, 
    request, 
    jsonify, 
    make_response,
    render_template
)

app = Flask(__name__)

#@app.route('/')
# @app.route('/moi/', defaults={'firstname': 'Sami', 'surname': 'Suomalainen'})
# @app.route('/moi/<firstname>', defaults={'surname': 'Suomalainen'})
@app.get(
        rule='/moi/<path:polku>/<firstname>/<int:age>/',
        # methods=['GET', 'POST'],
        endpoint='Matti',
        defaults=None,
        # strict_slashes=
        )
def moi(firstname, age, polku):
    return f'Moi {firstname}! You are {age} years old. Your path is: {polku}'
    # if request.method == 'GET':

@app.post(
        rule='/moi/<path:polku>/<firstname>/<int:age>/',
        # methods=['GET', 'POST'],
        endpoint='Matti_post',
        defaults=None,
        # strict_slashes=
        )
def moi(firstname, age, polku):
    return f'Moi. This is a response to a POST request.'

@app.route('/hello/', strict_slashes=False)
def hello():
    polku = url_for('Matti', age=50, firstname='Christian', polku='a/b/c')
    return f'Hello. The new address is {polku}'

@app.get('/params')
def params_get():
    username = request.args.get('username')
    return f'Parametrit: {request.args}.<br>Sinun käyttätunnus on {username}. Avain on: {request.args.getlist('avain')}'

@app.post('/params')
def params_post():
    return f'POST parameters: {request.form}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Login</h1>
    <form action="" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username">
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password">
        <br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''
    else:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username == 'christian' and password == 'Taitotalo1':
            return 'Login accepted'
        else:
            return 'Login failed'

@app.route('/json')
def json_funktio():
    return jsonify({'nimi': 'christian', 'age': 50})

@app.route('/custom')
def custom():
    # return make_response(iter(range(100000)))
    return make_response({'Error': 'Resource not found'}, 404)

@app.route('/')
def index():
    user = {'username': 'christian'}
    return render_template('index.html', username=user['username'], title='kotisivu')
#     return f'''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>Homepage</title>
# </head>
# <body>
#     <h1>Homepage</h1>
#     <p>Welcome back {user['username']}!</p>
# </body>
# </html>
# '''


if __name__ == '__main__':    
    app.run(debug=True)