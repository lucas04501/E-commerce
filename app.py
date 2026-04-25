# importação
from flask import Flask

app = Flask(__name__)

# definir uma rota raiz (initial page) e a function que sera executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

