from collections import deque

class Solution:
    def minMalwareSpread(self, grafo, inicial):
        n = len(grafo)
        inicial.sort()
        min_infectados = float('inf')
        no_resultado = inicial[0]

        def contar_infectados(no_removido):
            visitado = [False] * n
            fila = deque()
            contagem_infectados = 0

            for no in inicial:
                if no != no_removido:
                    fila.append(no)
                    visitado[no] = True

            while fila:
                atual = fila.popleft()
                contagem_infectados += 1
                for vizinho in range(n):
                    if grafo[atual][vizinho] == 1 and not visitado[vizinho]:
                        visitado[vizinho] = True
                        fila.append(vizinho)

            return contagem_infectados

        for no in inicial:
            infectados = contar_infectados(no)
            if infectados < min_infectados:
                min_infectados = infectados
                no_resultado = no

        return no_resultado

grafo = [[1,1,0],[1,1,0],[0,0,1]]
inicial = [0, 1, 2]
solucao = Solution()
print(solucao.minMalwareSpread(grafo, inicial))
