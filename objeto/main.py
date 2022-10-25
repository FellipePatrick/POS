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
    elif escolha == 3:
        id = str(input('Digite o id do usuario:(1 a 10)'))
        print(User.ler_us(id))
    elif escolha == 4:
        id = str(input('Digite o id do usuario:(1 a 10)'))
        print(User.deletar_us(id))
    elif escolha == 5:
        id = str(input('Digite o id do usuario:(1 a 10)'))
        userid = str(input('Digite o novo userId do usuario:'))
        title = str(input('Digite o titulo do novo usuario:'))
        dicionario = {"userId": userid, "title": title}
        print(User.atualiar_us(id, dicionario))
    elif escolha == 6:
        id = str(input('Digite o id do usuario que deseja criar a tarefa:(1 a 10)'))
        userid = str(input('Digite o novo userId da tarefa:'))
        title = str(input('Digite o titulo da nova tarefa:'))
        dicionario = {"userId": userid, "title": title}
        print(Tarefa.criar_t(id, dicionario))
    elif escolha == 7:
        id = str(input('Digite o id do usuario que deseja ver as tarefa:(1 a 10)'))
        print(Tarefa.ver_t(id))
    elif escolha == 8:
        id = str(input('Digite o id da tarefa que deseja atualizar:'))
        userid = str(input('Digite o userId para atualizar a tarefa:'))
        title = str(input('Digite o titulo para atualizar a tarefa:'))
        dicionario = {"userId": userid, "title": title}
        print(Tarefa.atualizar_t(id, dicionario))
    elif escolha == 9:
            id = str(input('Digite o id da tarefa que deseja deletar:'))
            print(Tarefa.delete_t(id))


pergunta = "sim"

while pergunta == "sim":
    menu()
    pergunta = input("Deseja continuar (sim ou não):")