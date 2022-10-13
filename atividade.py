import requests
api_url = "http://jsonplaceholder.typicode.com"

def todos():
    url = api_url + "/users"
    alluser = requests.get(url).json()
    cont = 0
    for i in alluser:
        cont = cont +1
        print(str(cont)+"-"+i['name'])
        

def ler_us():
    usuario2 = input('Qual usuario deseja verificar:')
    url = api_url + "/users{}".format(usuario2)
    response = requests.get(url)
    print(response.json())
    


def criar_us():
    url = api_url + "/users"
    todo = {"name":"Fellipe Patrick"}
    response = requests.post(url, json=todo)
    print(response.json())

def deletar_us():
    
    delet = input("Qual usuario deseja deletar?")
    url = api_url + "/posts/{}".format(delet)
    response = requests.delete(url)
    print(response.json())
    
def atualiar_us():
    
    att = input('Qual usuario deseja atualizar?')
    url = api_url + "/todos/{}".format(att)
    todo = {"userId": 1, "title": "Lavar carro", "completed": True}
    response = requests.put(url, json=todo)
    print(response.json())

lista = ['Criar Usuario', 'Ler Usuario', 'Deletar Usuario', 'Atualizar Usuario', 'Ver todos Usuario']

def menu():
    cont = 0
    for i in lista:
        cont = cont +1
        print(str(cont)+" - "+i)
    escolha = int(input())
        
menu()