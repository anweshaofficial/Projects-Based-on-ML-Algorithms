def dijkstra(graph, source, destination):
    queue = [source]
    distances = {source: 0}
    predecessors = {source: None}
    
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                predecessors[neighbor] = node
                queue.append(neighbor)
    
    if destination in distances:
        path = []
        current = destination
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]
        return path
    else:
        return []
    
# Test Cases for Djikstra Algorithm 

# Test Case 1
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
source = 'A'
destination = 'E'
print(dijkstra(graph, source, destination))  # Output: ['A', 'C', 'D', 'E']

# Test Case 2
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
source = 'B'
destination = 'E'
print(dijkstra(graph, source, destination))  # Output: ['B', 'D', 'E']

# Test Case 3
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
source = 'A'
destination = 'F'
print(dijkstra(graph, source, destination))  # Output: []

