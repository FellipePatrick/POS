import requests

api_url = "http://jsonplaceholder.typicode.com"

class User:    

    def ler_us(id):
        url = api_url + "/users/{}".format( str(id))
        response = requests.get(url)
        return response.json()
            
    def criar_us(nome):
        url = api_url + "/users"
        todo = {"name": str(nome)}
        response = requests.post(url, json=todo)
        return response.json()
    
    def deletar_us(id):
        delet = str(id)
        url = api_url + "/posts/{}".format(delet)
        response = requests.delete(url)
        return response.json()
    
    def atualiar_us(id, dicionario):
        url = api_url + "/todos/{}".format( str(id))
        todo = dicionario
        response = requests.put(url, json=todo)
        return response.json()
