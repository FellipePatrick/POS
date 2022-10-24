from usuario import User

from tarefa import Tarefa

lista = ['Ver todos Usuario','Criar Usuario', 'Ler Usuario', 'Deletar Usuario', 'Atualizar Usuario', 
         'Criar Tarefa', 'Ver Tarefa', 'Atualizar tarefa', 'Deletar tarefa']

def menu():
    cont = 0
    for i in lista:
        cont = cont +1
        print(str(cont)+" - "+i)
    escolha = int(input('Digite o que quer fazer:'))
    if escolha == 1:
        print(User.todos)
    elif escolha == 2:
        novouser = str(input('Digite o nome do novo usuario:'))
        dicionario = {'name': novouser}
        print(User.criar_us(dicionario))

        

pergunta = "sim"

while pergunta == "sim":
    menu()
    pergunta = input("Deseja continuar (sim ou não):")