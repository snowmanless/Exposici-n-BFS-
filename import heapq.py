import heapq

# Definir el grafo
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('A', 3), ('B', 2), ('D', 1), ('G', 4)],
    'D': [('B', 4), ('C', 1), ('E', 5), ('F', 6)],
    'E': [('D', 5)],
    'F': [('D', 6)],
    'G': [('C', 4)]
}

# Definir la heurística
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 7,
    'G': 0
}

def best_first_search(graph, start, goal, heuristic):
    # Cola de prioridad
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    # Conjunto de nodos explorados
    explored = set()
    
    # Diccionario para rastrear el camino
    came_from = {start: None}
    
    while priority_queue:
        # Extraer el nodo con la menor heurística
        _, current = heapq.heappop(priority_queue)
        
        if current == goal:
            # Reconstruir el camino
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Devolver el camino en el orden correcto
        
        explored.add(current)
        
        # Expandir los vecinos
        for neighbor, cost in graph[current]:
            if neighbor not in explored:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    
    return None  # Si no se encuentra un camino

# Ejemplo de uso
start = 'A'
goal = 'G'
path = best_first_search(graph, start, goal, heuristic)
print(f"Ruta desde {start} hasta {goal}: {path}")
