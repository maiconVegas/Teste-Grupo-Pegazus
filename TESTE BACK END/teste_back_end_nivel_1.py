#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

#############################   RESOLUÇÃO 1   #############################

produtos_30 = []

for loja in response:
    for produto in loja["produtos"]:
        if produto["preço"] > 30:
            produtos_30.append(produto)

# print(produtos_30)

# Explicão: Decidi realizar usando for pois ele percorre todas as lojas e seus produtos
# para identificar e realizar a condição do preço maior que 30.
# Além disso foi usado array para categorizar apenas produtos com a condição requisitado.
# E posteriormente sendo adicionado usando a função append()
# Usei esse tipo de solução pois é mais simples e claro evitando complexidades e equivocos de
# identificar produtos fora da condição
#########################################################################


#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

#############################   RESOLUÇÃO 2   #############################

produto_B_preco = 0

for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        produto_B_preco = produto["preço"]

# print(produto_B_preco)

# Explicão: Nesse caso realizando apenas 1 for para identificar os produtos 
# e depois realizar a condição de identificar o preço apenas do produto B.
# Escolhi esse tipo de solução pois é reaproveitado a semelhança da lógica do exercício
# anterior, além de alterar a lógica e sua condição. Ser simples e direto

#########################################################################

#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

#############################   RESOLUÇÃO 3   #############################

lista = sorted(lista)
# print(lista) # OU print(sorted(lista))

# Explicão: Nesse exercicio foi utilizado o método sorted() para classificar
# os elementos númericos de forma crescente. Escolhi essa solução para aproveitamento
# dessa solução existente no Python além de ser simples e rápido.

#########################################################################


#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

#############################   RESOLUÇÃO 4   #############################

nova_lista = []
for elemento in lista:
    nova_lista.append(elemento.strip())
# print(nova_lista)

# Explicão: Nesse exercicio foi utilizado o método strip para remover os 
# espaços em branco de cada elemento e posteriormente, adicionando elas
# na nova lista usando a função append().

#########################################################################

#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

#############################   RESOLUÇÃO 5   #############################

segundo_item = lista[1]
print(segundo_item)

# Explicão: Apenas usando o índice da lista como referência da posição do item

#########################################################################

#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#############################   RESOLUÇÃO 6   #############################

lista_semjoao = []
for nome in lista:
    lista_semjoao.append(nome.replace("joao", "maria"))
lista = lista_semjoao
# print(lista)

# Explicão: Nesse caso, foi usado o método replace() para realizar a 
# substituição do joao para maria

#########################################################################

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

#############################   RESOLUÇÃO 7   #############################

lista = ["item1", "item2", "item3","item4", "item5", "item6", "item7", "item8", "item9"]
x = 0
while x <= 5:
    print(lista[x])
    x += 1

# Explicão: Nesse exercicio, foi escolhido essa solução para explorar a lista 
# por sua índice. Além disso, foi impresso esses itens de acordo com seu valor da
# váriavel x para indicar as condições posteriores do while loop

#########################################################################

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

#############################   RESOLUÇÃO 8   #############################
import requests

def contarTasks():

    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if response.status_code == 200:
        tasks = response.json()
        completadas = 0
        pendentes = 0
        for task in tasks:
            if task["completed"] == True:
                completadas += 1
            elif task["completed"] == False:
                pendentes += 1
        return completadas, pendentes

    else:
        print("Erro no requests")
        return 0, 0
    
print(contarTasks())
# Explicão: Nesse exercicio, foi desenvolvido usando a biblioteca requests
# para ter a possibilidade de acessar o http json com seus respectivos dados
# do dicionário. Foi usado condições de sucesso de acesso para verificar caso
# tenha Erro de requests. Além disso foi usado a função json() para realizar
# desserialização tornando os dados como objetos para explorar as tasks completadas ou não.
# Motivo de escolher essa solução foi devido a praticidade do uso de dicionário local
# onde que possibilita a exploração desses dados localmente.
#########################################################################

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

#############################   RESOLUÇÃO 9   #############################
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        nome = user["name"]
        username = user["username"]
        email = user["email"]
        rua = user["address"]["street"]
        numero = user["phone"]
        print(nome, username, email, rua, numero)

# Explicão: Nesse caso, foi retirados dados através da API usando o requests.
# posteriormente foi realizado o processo de parsing para desserialização do Json.
# posteriormente foi usado o for para realizar a buscas dos dados chaves de acordo que foi requisitado.
# Foi usado essa solução pois tem mais implementações de opções para realizar as buscas chaves e seus respectivos dados.
# Além de que foi reaproveitado tendo proximidades semelhanças com o exercicio anterior.

#########################################################################

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

#############################   RESOLUÇÃO 10   #############################

import queue
lista = []
lista = queue.Queue()
lista.put("item1")

#########################################################################

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

#############################   RESOLUÇÃO 11   #############################

import queue
lista = []
lista = queue.LifoQueue()
lista.put("item1")

#########################################################################

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

#############################   RESOLUÇÃO DESAFIO   ############################# 

import abc

class IBanco(abc.ABC):
    
    @abc.abstractmethod
    def sacar(self, valor):
        pass

    @abc.abstractmethod
    def depositar(self, valor):
        pass
    
    
class Banco(IBanco):
    autoin = 0
    def __init__(self, nome, cpf):
        if not nome or not cpf:
            raise ValueError("Nome e/ou Cpf não podem estar vazios")
        Banco.autoin += 1
        self.id = Banco.autoin
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.00

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        elif valor > self.saldo:
            print("Saldo insuficiente")
            return
        else: 
            self.saldo -= valor
            print("Saque realizado")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        else:
            self.saldo += valor
            print("Depósito realizado")

#########################################################################