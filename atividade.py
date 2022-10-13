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
    name2 = input('Digite o nome para alterar:')
    todo = {"name": name2}
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
    Id2 = input('Digite o novo ip para atualizalo')
    title2 = input('Digite o novo titulo para atualizalo')
    todo = {"Id": Id2, "title": title2 }
    response = requests.put(url, json=todo)
    print(response.json())
    
def criar_t():
    id1 = input('Digite o id que você quer alterar:')
    url = api_url +'/users'+{}+ "/todos".format(id1)
    response = requests.get(url)
    print(response.json['id'])
    

lista = ['Criar Usuario', 'Ler Usuario', 'Deletar Usuario', 'Atualizar Usuario', 'Ver todos Usuario']

def menu():
    cont = 0
    for i in lista:
        cont = cont +1
        print(str(cont)+" - "+i)
    escolha = int(input('Digite o que quer fazer:'))
    if escolha == 1:
        criar_us()
    elif escolha == 2:
        ler_us()
    elif escolha == 3:
        deletar_us()
    elif escolha == 4:
        atualiar_us()
    elif escolha == 5:
        todos()

pergunta = "sim"

while pergunta == "sim":
    menu()
    pergunta = input("Deseja continuar (sim ou não):")
    

