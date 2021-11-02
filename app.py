from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_Id = request.remote_addr

    response = make_response(redirect('/hello/'))
    response.set_cookie('user_Id', user_Id)

    return response

@app.route('/hello/')
def hello():
    user_Id = request.cookies.get('user_Id')
    return f'Hello tu ip es: {user_Id}'



if __name__ == '__main__':
    app.run(debug=True, port = 5000)