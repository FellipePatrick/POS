import requests
api_url = "http://jsonplaceholder.typicode.com"

class Metodo: 
    def __init__(self, criar):
        self.url = api_url + "/users"
        self.name2 = input('Digite o nome para alterar:')
        self.todo = {"name": self.name2}
        self.response = requests.post(self.url, json=self.todo)
        self.criar = print(self.response.json())
