graph = [
    ['J', 'K', 146,668],
    ['J', 'I', 172,499],
    ['J', 'E', 105,500],
    ['K', 'L', 152,300],
    ['E', 'L', 110,300],
    ['E', 'A', 133,221],
    ['I', 'A', 109,221],
    ['I', 'C', 102,400],
    ['L', 'O', 97,170],
    ['A', 'O', 151,170],
    ['A', 'D', 43,326],
    ['C', 'D', 126,326],
    ['I', 'C', 102,400],
    ['C', 'B', 171,350],
    ['O', 'M', 100,78],
    ['I', 'C', 102,400],
    ['D', 'O', 136,170],
    ['D', 'M', 200,78],
    ['D', 'F', 111,209],
    ['B', 'G', 171,188],
    ['G', 'C', 140,400],
    ['G', 'D', 123,326],
    ['G', 'H', 99,92],
    ['F', 'G', 88,188],
    ['F', 'H', 130,92],
    ['H', 'N', 80,0],
    ['M', 'N', 67,0]
]
temp = []
temp1 = []
for i in graph:
    temp.append(i[0])
    temp1.append(i[1])
nodes = set(temp).union(set(temp1))


def A_star(graph, costs, open, closed, cur_node):
    if cur_node in open:
        open.remove(cur_node)
    closed.add(cur_node)
    for i in graph:
        if (i[0] == cur_node and costs[i[0]]+i[2]+i[3] < costs[i[1]]):
            open.add(i[1])
            costs[i[1]] = costs[i[0]]+i[2]+i[3]
            path[i[1]] = path[i[0]] + ' -> ' + i[1]
    costs[cur_node] = 999999
    small = min(costs, key=costs.get)
    if small not in closed:
        A_star(graph, costs, open, closed, small)


costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
    costs[i] = 999999
    path[i] = ' '
open = set()
closed = set()
start_node = input("Enter the Start Node: ")
open.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
A_star(graph, costs, open, closed, start_node)
goal_node = input("Enter the Goal Node: ")
print("Path with least cost is: ", path[goal_node])
