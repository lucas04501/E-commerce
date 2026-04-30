# importação
from flask import Flask, request, jsonify
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
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'})
    return jsonify({'message': 'Invalid product data'}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    # recuperar o produto da base de dados usando o id fornecido. se o produto existir, ele é deletado e a mudança é salva no banco de dados. se o produto não for encontrado, uma mensagem de erro é retornada.
    # verificar se o produto existe usando o método query.get() do SQLAlchemy. se o produto existir, ele é deletado usando db.session.delete() e as mudanças são salvas no banco de dados usando db.session.commit(). se o produto não for encontrado, uma mensagem de erro é retornada com um status code 404 (Not Found).
    # se existe, o produto é deletado usando db.session.delete(product) e as mudanças são salvas no banco de dados usando db.session.commit(). se o produto não for encontrado, uma mensagem de erro é retornada com um status code 404 (Not Found).
    # se nao existe, uma mensagem de erro é retornada com um status code 404 (Not Found).
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'message': 'Product not found'}), 404

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    return jsonify({'message': 'Product not found'}), 404

# definir uma rota raiz (initial page) e a function que sera executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

