import requests
api_url = "http://jsonplaceholder.typicode.com"

def criar_t():
    id1 = input(str('Digite o id que você quer alterar:'))
    url = api_url +'/users/{}'+ "/todos".format(id1)
    response = requests.get(url)
    print(type(response))
    
print ('hello')