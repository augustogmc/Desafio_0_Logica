#Exercício 1

#Entrada da quantidade dos asteriscos desejados.
n = int(input('digite a quantidade de asteriscos que deseja: '))

def criar_lista_asteriscos(n):
    lista = []  # Cria uma lista vazia para armazenar as strings.
    for i in range(1, n + 1):  # Loop de 1 até n.
        asteriscos = '*' * i  # Cria uma string com i asteriscos.
        lista.append(asteriscos)  # Adiciona a string à lista.
    return lista  # Retorna a lista resultante.

resultado = criar_lista_asteriscos(n)  # Chama a função igual a n.
print(resultado)








