import requests
api_url = "http://jsonplaceholder.typicode.com"

class Tarefa:
    def __init__(self, id, criar_t, oid):
        self.id = ''
        self.oid = ''
        url = api_url +'/users/'+self.id+'/todos'
        todo = {"Id": self.oid}
        response = requests.post(url, json=todo)
        self.criar_t = print(response.json())
        
    def __init__(self, deletar_t, id):
        self.id = ''
        url = api_url +"/todos/" + self.id
        response = requests.delete(url)
        self.deletar_t = print(response.json())
  
    def __init__(self, UserId, title, id, atualizar_t):
        self.id = ''
        url = api_url +'/todos/'+self.id
        self.UserId = ''
        self.title = ''
        todo = {"userId": self.UserId, "title": self.title, "completed": True}
        response = requests.put(url, json=todo)
        self.atualizar_t = print(response.json())

