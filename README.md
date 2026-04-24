# 🛒 E-commerce API (Flask & Python)

Esta API simula o backend completo de um sistema de e-commerce. Desenvolvida com **Python** e o framework **Flask**, a aplicação gerencia desde a autenticação de usuários até o fluxo de compras, permitindo a manipulação de produtos e a organização de um carrinho virtual.

---

## 📌 Funcionalidades Principais

* **Gestão de Identidade:** Sistema de login e logout com controle de sessão.
* **Catálogo Dinâmico:** Listagem completa, busca por palavras-chave e visualização de detalhes de produtos.
* **Operações Administrativas:** Suporte completo para Criar, Atualizar e Deletar produtos (CRUD).
* **Fluxo de Consumo:** Adição de itens ao carrinho, visualização de itens selecionados e processo de checkout.

---

## 🛠️ Tecnologias e Arquitetura

* **Linguagem:** Python 3.x
* **Framework:** Flask
* **Documentação:** Swagger 2.0
* **Ambiente:** Host local (127.0.0.1:5000)

---

## 🗄️ Arquitetura de Dados

O projeto utiliza um modelo relacional para gerenciar as informações do e-commerce. A estrutura de objetos definida segue esta lógica:

* **Relacionamento Usuário-Carrinho:** Cada usuário possui um carrinho (`cart`) que armazena uma lista de itens.
* **Entidade de Produto:** Armazena os dados fundamentais como `id`, `name`, `price` e `description`.
* **Vínculo de Transação (CartItem):** Atua como a ponte entre o usuário (`user_id`) e o produto (`product_id`), permitindo o rastreamento de quais itens pertencem a cada conta.

---

## 🛣️ Documentação dos Endpoints

Abaixo estão as rotas mapeadas conforme a estrutura da API:

### 🔐 Autenticação
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/login` | Autentica o usuário (exige `username` e `password`). |
| `POST` | `/logout` | Encerra a sessão do usuário atual. |

### 📦 Catálogo de Produtos
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/products` | Lista todos os produtos disponíveis. |
| `GET` | `/api/products/{id}` | Retorna detalhes técnicos de um produto específico. |
| `GET` | `/api/products/search` | Busca produtos via query string (`?q=nome`). |
| `POST` | `/api/products/add` | Adiciona um novo produto ao catálogo. |
| `PUT` | `/api/products/update/{id}` | Atualiza as informações de um produto existente. |
| `DELETE` | `/api/products/delete/{id}` | Remove permanentemente um produto do sistema. |

### 🛍️ Carrinho & Checkout
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/cart` | Exibe o conteúdo atual do carrinho do usuário. |
| `POST` | `/api/cart/add/{id}` | Adiciona um item específico ao carrinho. |
| `DELETE` | `/api/cart/remove/{id}` | Remove um item do carrinho através do seu ID de item. |
| `POST` | `/api/cart/checkout` | Finaliza a compra e limpa o carrinho. |

---

## 🏗️ Modelos de Dados (Schema)

A API trabalha com três entidades principais:

* **User:** ID, username, password e lista de itens no carrinho.
* **Product:** ID, nome, preço e descrição.
* **CartItem:** ID único do item, ID do usuário (`user_id`) e ID do produto (`product_id`).

---

## 🚀 Como testar

1. Certifique-se de ter o **Python** e o **Flask** instalados.
2. Inicie o servidor local através do VS Code ou terminal.
3. Utilize ferramentas como **Postman** ou **Insomnia** para realizar as requisições para `http://127.0.0.1:5000`.