color = {"A":'white',"B":'white',"C":'white',"D":'white',"E":'white'}
right = {}
left = {}
turn = "left"
ispartite = True
def isbipartite_dfs(graph): 
    for start in graph:
        if color[start] == "white":
            _isbipartite_dfs(start, graph)
    if ispartite==True:
        print "LEFT: " , left.values(), "  RIGHT:" , right.values()  
    else:
        print "NOT PARRTITE"
    
    
    
def _isbipartite_dfs(start, graph):
    global right, left
    global ispartite
    global turn
    color[start] = 'gray'
    if turn =="left":
        left[len(left)+1] = start
        turn = "right"
    else:
        right[len(right)+1] = start
        turn = "left"
    if start not in graph:
        color[start] = 'black'
        if turn=="left":
            turn ="right"
        else:
            turn = "left"
        return
    for n in graph[start]:
        if color[n] != 'black':
            _isbipartite_dfs(n, graph)
        elif turn == "right" and n in left.values():
            ispartite = False
            return
        elif turn == "left" and n in right.values():
            ispartite = False
            return
    color[start] = 'black'
    if turn=="left":
        turn ="right"
    else:
        turn = "left"            
    
    
        

if __name__ == "__main__":
    graph = {"A": ["D", "E"], "B": ["D"], "C": ["E"]}
#     graph = {"A": ["D", "E"], "B": ["D"], "C": ["A","E"]}
    isbipartite_dfs(graph)
