# API de e-commerce (Python e Flask)

Projeto de estudo: o backend de uma loja virtual feito com **Python** e **Flask**. Hoje a API já faz login e logout, gerencia o catálogo de produtos (cadastrar, listar, ver, atualizar e remover) e adiciona produtos ao carrinho do usuário logado. Busca, consulta e remoção de itens do carrinho, finalização da compra e documentação Swagger ainda **não** estão implementadas (ver "Próximos passos").

## O que funciona hoje

* **Autenticação:** login e logout com sessão, usando Flask-Login.
* **Catálogo:** listagem pública de produtos; detalhe, cadastro, atualização e remoção exigem login.
* **Carrinho:** adicionar um produto ao carrinho do usuário logado.
* **Dados:** SQLite com SQLAlchemy (usuário, produto e item de carrinho).

## Como rodar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

A API sobe em `http://127.0.0.1:5000` e cria o banco (`instance/ecommerce.db`) na primeira execução. Para ligar o modo de depuração, use `FLASK_DEBUG=1`. A chave de sessão vem de `SECRET_KEY` (sem ela, vale um valor só para desenvolvimento).

### Criar um usuário para testar

Ainda não existe rota de cadastro. Crie um usuário pelo shell do Flask:

```bash
flask --app app shell
>>> from app import db, User
>>> db.session.add(User(username="teste", password="uma-senha-de-teste")); db.session.commit()
```

Depois faça `POST /login` com `{"username": "teste", "password": "uma-senha-de-teste"}`. As rotas protegidas redirecionam para `/login` quando não há sessão.

## Endpoints implementados

| Método | Endpoint | Login | Descrição |
| :--- | :--- | :---: | :--- |
| `POST` | `/login` | não | Autentica (`username` e `password`). |
| `POST` | `/logout` | sim | Encerra a sessão. |
| `GET` | `/api/products` | não | Lista os produtos (`id`, `name`, `price`). |
| `GET` | `/api/products/{id}` | sim | Detalhe de um produto. |
| `POST` | `/api/products/add` | sim | Cadastra um produto (`name`, `price`, `description` opcional). |
| `PUT` | `/api/products/update/{id}` | sim | Atualiza campos de um produto. |
| `DELETE` | `/api/products/delete/{id}` | sim | Remove um produto. |
| `POST` | `/api/cart/add/{id}` | sim | Adiciona o produto ao carrinho do usuário logado. |

## Modelo de dados

* **User:** `id`, `username`, `password` e a relação `cart`.
* **Product:** `id`, `name`, `price`, `description`.
* **CartItem:** liga um usuário (`user_id`) a um produto (`product_id`).

## Próximos passos

* Busca de produtos por palavra-chave.
* Consultar o carrinho e remover itens.
* Finalizar a compra (checkout). O projeto ainda não tem integração com pagamento.
* Cadastro de usuários e senhas com hash (hoje a senha é guardada e comparada em texto puro: é um projeto de estudo, não use em produção).
* Documentação da API (Swagger).
* Testes automatizados.
