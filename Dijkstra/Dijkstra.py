def dijkstra(grafo,chave,destino,visitado=[],distancia={},anterior={}):
    """ Calcula a menor rota
    """    
    # algumas checagens
    if chave not in grafo:
        raise TypeError('a raiz da arvore de caminho mais curto nao pode ser encontrado no grafo')
    if destino not in grafo:
        raise TypeError('o alvo do caminho mais curto nao pode ser encontrado no grafo')    
    # finalizando a condicao
    if chave == destino:
        # Contruir o caminho e mostramos ele
        caminho = []
        ant = destino
        while ant != None:
            caminho.append(ant)
            ant = anterior.get(ant,None)
        print('Menor caminho: ' + str(caminho) + " andou = " + str(distancia[destino])) 
    else :     
        # se eh a execucao inicial inicializa a procura
        if not visitado: 
            distancia[chave] = 0
        # procura nos vizinhos
        for vizinho in grafo[chave] :
            if vizinho not in visitado:
                nova_distancia = distancia[chave] + grafo[chave][vizinho]
                if nova_distancia < distancia.get(vizinho,float('inf')):
                    distancia[vizinho] = nova_distancia
                    anterior[vizinho] = chave
        # marca como visitado
        visitado.append(chave)
        # agora todos os vizinhos foram visitados
        # seleciona o vertice nao visitado com a menor distancia
        # executa recursivamente o dijkstra
        naovisitados = {}
        for chav in grafo:
            if chav not in visitado:
                naovisitados[chav] = distancia.get(chav,float('inf'))        
        x = min(naovisitados, key=naovisitados.get)
        dijkstra(grafo,x,destino,visitado,distancia,anterior)
        


if __name__ == "__main__":

    #grafo
    grafo = {'s': {'c': 1, 'b': 3},
            'c': {'s': 1, 'f': 5, 'd': 2},
            'd': {'b': 1, 'c': 2,'e': 4,'f': 2},
            'e': {'d': 4, 'h': 1, 'g': 2},
            'f': {'c': 5, 'h': 3, 'd': 2},
            'g': {'e': 2, 'b': 5},
            'h': {'e': 1, 'f': 3}}

    #grafos e a distancia entre cada vertices
    #inicia o grafo e ponto de origem e ponto final
    dijkstra(grafo,'s','h')
