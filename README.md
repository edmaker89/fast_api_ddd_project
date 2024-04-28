# API de Produtos com MongoDB e FastAPI

Este projeto consiste em uma API de produtos que utiliza o MongoDB como banco de dados e é desenvolvida com o framework FastAPI. O desenvolvimento é baseado em Test-Driven Development (TDD), o que significa que os testes são escritos antes da implementação do código.

## Funcionalidades da API

- Cadastro de novos produtos com informações como nome, descrição e preço.
- Recuperação de todos os produtos cadastrados.
- Filtragem de produtos por faixa de preço.
- Atualização de informações de um produto específico.
- Exclusão de um produto do banco de dados.

## Tecnologias Utilizadas

- **FastAPI**: Framework web rápido para construir APIs com Python.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os dados dos produtos.
- **Pydantic**: Biblioteca para validação de dados e serialização.
- **pytest**: Framework de teste para escrever e executar testes automatizados.
- **PyMongo**: Biblioteca Python para interagir com o MongoDB.

## Estrutura do Projeto

A estrutura do projeto segue um padrão comum para aplicações FastAPI:

- `main.py`: Arquivo principal que contém a configuração da aplicação FastAPI.
- `models.py`: Definição dos modelos de dados utilizando Pydantic.
- `controller.py`: Implementação das rotas e lógica de negócio da API.
- `database.py`: Configuração e conexão com o banco de dados MongoDB.
- `tests/`: Diretório contendo os testes unitários escritos com pytest.
- `requirements.txt`: Arquivo que lista as dependências do projeto.

## Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório do projeto.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Inicie o servidor FastAPI executando o arquivo `main.py`.
4. Acesse a documentação da API em `http://localhost:8000/docs` para interagir com os endpoints.

## Testes

Os testes unitários são escritos utilizando o framework pytest e estão localizados no diretório `tests/`. Eles abrangem a cobertura de funcionalidades como cadastro, consulta e filtragem de produtos, garantindo a qualidade e robustez do código.

## Conclusão

Este projeto demonstra a criação de uma API de produtos com MongoDB e FastAPI, seguindo as práticas de TDD para garantir um desenvolvimento mais seguro e confiável. A estrutura modular e os testes abrangentes contribuem para a manutenção e evolução da aplicação.
