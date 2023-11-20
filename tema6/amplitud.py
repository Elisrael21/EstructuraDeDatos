from collections import defaultdict, deque

# Clase para representar un objeto grafo
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Función para agregar una arista al grafo
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Función para realizar la búsqueda en amplitud en el grafo
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Ejemplo de uso
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('C', 'G')
graph.add_edge('D', 'H')
graph.add_edge('D', 'I')
graph.add_edge('E', 'J')
graph.add_edge('E', 'K')
graph.add_edge('F', 'L')
graph.add_edge('F', 'M')

print("Recorrido en amplitud:")
graph.bfs('A')
