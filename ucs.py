def uniform_cost_search(graph, start, goal):
    queue = [(0, [start])]
    visited = set()
    
    while queue:
        queue.sort()
        cost, path = queue.pop(0)
        node = path[-1]
  
        if node in visited:
            continue
            
        visited.add(node)
        
        if node == goal:
            return path, cost
        
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                queue.append((new_cost, new_path))
    
    return None, float('inf')
graph = {
    'A': [('B', 1), ('C', 4)], 
    'B': [('D', 5), ('E', 2)], 
    'C': [('F', 1)], 
    'D': [], 
    'E': [('G', 3)], 
    'F': [], 
    'G': []
}
path, cost = uniform_cost_search(graph, 'A', 'G')
print("Shortest path:", path)
print("Total cost:", cost)