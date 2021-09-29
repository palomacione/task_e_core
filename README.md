# Desafio Técnico E-Core
Nesse desafio, usamos a linguagem Python e criamos a classe Person, feita para criar objetos que representam as pessoas a serem adicionadas, assim como a classe Control que executa nossas funcionalidades. Temos também uma UI simples feita com PyQt e endpoints disponíveis, criados com Flask, para requisições (enviadas por json).

## Funções Implementadas 
- Adiciona uma pessoa com nome e idade numa lista
- Retorna a lista de pessoas em ordem alfabética ou por ordem de idade
- Classifica as pessoas em crianças, adolescentes, idosos ou adultos. 

## Execução

Apenas teremos duas depências: PyQt para a parte gráfica (UI) e Flask para a parte REST. Podemos executar então como:
- ``` git clone https://github.com/palomacione/task_e_core ```
- ``` cd task_e_core ```
- ``` pip install pyqt5 ```
- ``` pip install Flask ```
- ```python main.py (para rodar com parte gráfica) ou python routes.py (para fazer as requisições HTTP)```