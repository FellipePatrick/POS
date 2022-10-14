from urllib import response
import requests
api_url = "http://jsonplaceholder.typicode.com"

def criar_t():
    id = str(input('Digite o id que você quer alterar:'))
    url = api_url +'/users/'+id+ "/todos"
    responsecheck = requests.get(url)
    response = requests.get(url).json()
    if responsecheck.status_code== 200:
        for task in response:
            print('Título: ', task['title'])
            print('ID', task['id'])
            print('Status: ', task['completed'])
            print()
     
       

criar_t()