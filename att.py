from urllib import response
import requests
api_url = "http://jsonplaceholder.typicode.com"

def criar_t():
    id = str(input("Digite o ID em que quer criar uma tarefa:"))
    url = api_url +'/users/'+id+'/todos'
    todo = {"Id": 1}
    response = requests.post(url, json=todo)
    print(response.json())
    
def ver_t():
    id = str(input('Tarefa de quais atividades você quer ver?'))
    url = api_url +'/users/'+id+ "/todos"
    responsecheck = requests.get(url)
    response = requests.get(url).json()
    if responsecheck.status_code== 200:
        for task in response:
            print('Título: ', task['title'])
            print('ID', task['id'])
            print('Status: ', task['completed'])           

def delete_t():
    id = str(input('Tarefa que deseja deletar?'))
    url = api_url +'/users/'+id+ "/todos"
    response = requests.delete(url)
    print(response.json())
    print(response.status_code)
    
def atualizar_t():
    id = str(input('Tarefa que deseja atualizar?'))
    url = api_url +'/todos/'+id
    todo = {"userId": 1, "title": "Lavar carro", "completed": True}
    response = requests.put(url, json=todo)
    print(response.json())
    print(response.status_code)


