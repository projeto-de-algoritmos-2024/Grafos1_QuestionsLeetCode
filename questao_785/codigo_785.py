from collections import deque

class Solution:
    def isBipartite(self, grafo):
        n = len(grafo)
        cores = [-1] * n

        def bfs(inicio):
            fila = deque([inicio])
            cores[inicio] = 0
            while fila:
                no = fila.popleft()
                for vizinho in grafo[no]:
                    if cores[vizinho] == -1:
                        cores[vizinho] = 1 - cores[no]
                        fila.append(vizinho)
                    elif cores[vizinho] == cores[no]:
                        return False
            return True

        for i in range(n):
            if cores[i] == -1:
                if not bfs(i):
                    return False
        return True
