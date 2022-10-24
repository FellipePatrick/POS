import requests
api_url = "http://jsonplaceholder.typicode.com"

class Tarefa:
   
    def criar_t(id, dicionario):
        url = api_url +'/users/'+str(id)+'/todos'
        todo = dicionario
        response = requests.post(url, json=todo)
        return response.json()
   
    def ver_t(id):
        url = api_url +"/todos/"+str(id)+ "/todos/"
        responsecheck = requests.get(url)
        response = requests.get(url).json()
        if responsecheck.status_code == 200:
            for task in response:
                print('Título: ', task['title'])
                print('ID', task['id'])
                print('Status: ', task['completed'])
    
    def delete_t(id):
        url = api_url +"/todos/" + str(id)
        response = requests.delete(url)
        print(response.json())
        print(response.status_code) 
        
    def atualizar_t(id):
        url = api_url +'/todos/'+ str(id)
        todo = {"userId": 1, "title": "Lavar carro", "completed": True}
        response = requests.put(url, json=todo)
        print(response.json())
        print(response.status_code)          