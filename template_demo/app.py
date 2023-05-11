from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home', heading='標題', content='網站內容')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

