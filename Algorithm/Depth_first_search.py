
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def DFS_recursive(graph, node, path = []):
    # O(v + e) Time | O(v) Space

    if node not in path:
        path.append(node)
        for child in graph[node]:
            DFS_recursive(graph, child, path)

    return path

DFS_recursive(graph, 'A')
