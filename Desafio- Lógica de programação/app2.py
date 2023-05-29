def encontrar_pares_menor_diferenca(array):
    array_ordenado = sorted(array)  # Ordena o array em ordem crescente.
    menor_diferenca = float('inf')  # Inicializa a menor diferença com um valor infinito.
    pares_menor_diferenca = []  # Lista para armazenar os pares com menor diferença.

    # Percorre o array ordenado, comparando cada número com o próximo.
    for i in range(len(array_ordenado) - 1):
        diferenca = abs(array_ordenado[i] - array_ordenado[i+1])  # Calcula a diferença absoluta.

        # Verifica se a diferença é menor que a menor diferença encontrada até o momento.
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca  # Atualiza a menor diferença.
            pares_menor_diferenca = [(array_ordenado[i], array_ordenado[i+1])]  # Atualiza a lista de pares.
        elif diferenca == menor_diferenca:
            pares_menor_diferenca.append((array_ordenado[i], array_ordenado[i+1]))  # Adiciona o par à lista.

    return pares_menor_diferenca

# Solicita a entrada dos array.
entrada = input("Digite os números separados por espaço: ")

# Converte a entrada do usuário em uma lista de inteiros.
array = list(map(int, entrada.split()))

# Atribuindo o valor da função ao resultado.
resultado = encontrar_pares_menor_diferenca(array)

print(resultado)
