graph = {
 'J':['I','E','K'],
 'I':['C','A'],
 'E':['A','L'],
 'K':['E','L'],
 'C':['B','D'],
 'A':['D','O'],
 'L':['O'],
 'B':['G'],
 'D':['F','M','O'],
 'O':['M'],
 'G':['C','D','H'],
 'F':['G','H'],
 'M':['N'],
 'H':['N'],
 'N':[]

}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'J')    # function calling
print("\n")