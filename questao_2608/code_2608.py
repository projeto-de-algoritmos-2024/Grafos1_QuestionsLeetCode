from collections import deque

class Solution:
    def findShortestCycle(self, n, edges):
        # cria uma lista de adjacências para representar o grafo
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # função BFS para encontrar o menor ciclo começando de um nó específico
        def bfs(start):
            # cria uma lista de distâncias, -1 significa que o nó ainda não foi visitado
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            
            min_cycle = float('inf')
            while q:
                node = q.popleft()
                # percorre todos os vizinhos do nó atual
                for neighbor in graph[node]:
                    if dist[neighbor] == -1:
                        # se o vizinho ainda não foi visitado, atualiza a distância e adiciona à fila
                        dist[neighbor] = dist[node] + 1
                        q.append(neighbor)
                    elif dist[neighbor] >= dist[node]:
                        # se encontrar um vizinho que já foi visitado, pode ser um ciclo
                        min_cycle = min(min_cycle, dist[node] + dist[neighbor] + 1)
            return min_cycle
        
        # percorre todos os nós para tentar encontrar o menor ciclo possível
        result = float('inf')
        for i in range(n):
            result = min(result, bfs(i))
        
        # se não encontrou ciclo, retorna -1, senão retorna o menor ciclo encontrado
        return -1 if result == float('inf') else result

n = 7
edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [3, 6]]
solution = Solution()
print(solution.findShortestCycle(n, edges))
