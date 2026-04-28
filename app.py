# importação
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# definindo o modelo de dados para os produtos. no meu produto tem (id, name, price e description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)    # nullable= False significa que o campo é obrigatório. diz se é opcional ou nao(se for true, diz que nullable é opcional)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


@app.route('/api/products/add' , methods=['POST'])
def add_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
    db.session.add(product)
    db.session.commit()
    return 'Product added successfully'

# definir uma rota raiz (initial page) e a function que sera executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

