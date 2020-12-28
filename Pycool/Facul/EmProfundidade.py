visitados = set()
lista = []


def EmProfundidade(visitado, grafo, no):
    if no not in visitado:
        lista.append(no)
        visitado.add(no)
        for vizinho in grafo[no]:
            EmProfundidade(visitado, grafo, vizinho)


def EmProfundidade2(grafo, no):
    pilha, caminho = [no], []

    while pilha:
        vertice = pilha.pop()
        if vertice in caminho:
            continue
        caminho.append(vertice)
        for neighbor in grafo[vertice]:
            pilha.append(neighbor)

    return caminho


grafo = {
    'A': ['B', 'E', 'H', 'I'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['C', 'F', 'G'],
    'E': ['A', 'C', 'H', 'J'],
    'F': ['C', 'D', 'G'],
    'G': ['D', 'F'],
    'H': ['A', 'E', 'I', 'J', 'K'],
    'I': ['A', 'H', 'K'],
    'J': ['E', 'H'],
    'K': ['H', 'I']
}


EmProfundidade(visitados, grafo, 'A')
print(lista)

visitados2 = EmProfundidade2(grafo, 'A')
print(visitados2)
