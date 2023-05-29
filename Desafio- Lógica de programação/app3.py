def retornar_subconjunto():
    entrada = [1, 2]

    subconjuntos = [[]]  # Começamos com um subconjunto vazio

    for num in entrada:
        # Para cada número no conjunto de entrada, criamos novos subconjuntos
        # adicionando o número a cada um dos subconjuntos existentes.
        novos_subconjuntos = []     
        for subconjunto in subconjuntos:
            novos_subconjuntos.append(subconjunto + [num])
        subconjuntos.extend(novos_subconjuntos)

    return subconjuntos #Retornando os subconjuntos 

resultado = retornar_subconjunto() #Atribuindo a função ao resultado.
print(resultado)