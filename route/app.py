from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/greet/<name>')
# 字符串（默认）： 匹配任意字符串。
def greet(name):
    return f'Hello, {name}!'

@app.route('/user/<int:user_id>')
# 整数（<int:name>）： 匹配整数值。
def user_profile(user_id):
    return f'User ID: {user_id}'

@app.route('/files/<path:filename>')
# 匹配包含斜杠的路径 filename。
def serve_file(filename):
    return f'Serving file: {filename}'

@app.route('/float/<float:value>')
# 浮点数（<float:value>）： 匹配浮点数值。
def float_value(value):
    return f'Float value: {value}'

if __name__ == '__main__':
    app.run(debug=True)