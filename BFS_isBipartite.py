color = {"A":'white',"B":'white',"C":'white',"D":'white',"E":'white'}

right = {}
left = {}
turn = "left"
ispartite = True
q = []
visit = ""
back = ""
cross = ""
def isbipartite_bfs(graph):
    global right
    global left
    global turn
    global ispartite
    root=""
    
    for n in graph:
        if color[n]=="white":
            q.extend(n)
        while q!=[]:
            if q[0] =="l":
                turn = "left"
                q.pop(0)
                root = q.pop(0)
                node = q.pop(0)
            elif q[0] =="r":
                turn = "right"
                q.pop(0)
                root = q.pop(0)
                node = q.pop(0)
            else:
                node = q.pop(0)
            if node not in graph and color[node]!="black":
                color[node] = "black"
            elif color[node] == "white":
                root = node
                color[node] = "gray"
                if turn == "left":
                    left[len(left)+1] = root
                    for i in graph[node]:
                        if i not in right.values():
                            if i in left.values():
                                ispartite = False
                            else:
                                right[len(right)+1]=i
                    q.extend("r")
                    turn = "right"
                else:
                    
                    right[len(right)+1]=root
                    for i in graph[node]:
                        if i not in left.values():
                            if i in right.values():
                                ispartite =False
                            else:
                                left[len(left)+1]=i
                    q.extend("l")
                    turn = "left"
                
                q.extend(root)
                q.extend(graph[node])
            
        if turn == "left":
            turn = "right"
        else:
            turn = "left"
            
    if ispartite == True:
        print "LEFT: ", left.values(), " RIGHT: ", right.values()
    else:
        print "not partite"
    
        
if __name__ == "__main__":
#     graph = {"A": ["D", "E"], "B": ["D"], "C": ["E"]}
    graph = {"A": ["D", "E"], "B": ["D"], "C": ["A","E"]}
    isbipartite_bfs(graph)
