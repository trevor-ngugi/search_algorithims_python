# Using a Python dictionary to act as an adjacency list
graph = {
    'J': ['I', 'E', 'K'],
    'I': ['C', 'A'],
    'E': ['A', 'L'],
    'K': ['E', 'L'],
    'C': ['B', 'D'],
    'A': ['D', 'O'],
    'L': ['O'],
    'B': ['G'],
    'D': ['F', 'M', 'O'],
    'O': ['M'],
    'G': ['C', 'D', 'H'],
    'F': ['G', 'H'],
    'M': ['N'],
    'H': ['N'],
    'N': []
}

visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'J')
