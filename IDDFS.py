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
def DLS(start,goal,path,level,maxD):
    print('nCurrent level-->',level)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level==maxD:
        return False
    print('nExpanding the current node',start)
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False
start = 'J'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")