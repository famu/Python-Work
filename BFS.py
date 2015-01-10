color = {"A":'white',"B":'white',"C":'white',"D":'white',"E":'white'}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}

q = []
visit = ""
back = ""
cross = ""
root = ""
def bfs():
    global visit
    global back
    global cross
    global root
    for n in graph:
        if color[n]=="white":
            q.extend(n)
        while q!=[]:
            if q[0] =="!":
                q.pop(0)
                root = q.pop(0)
                node = q.pop(0)
            else:
                node = q.pop(0)
            if node not in graph and color[node]!="black":
                visit = visit + " " + node
                color[node] = "black"
            elif color[node] == "white":
                visit = visit + " " + node
                color[node] = "gray"
                q.extend("!")
                q.extend(node)
                q.extend(graph[node])
            elif color[node] == "gray":
                back = back +  root + "->" + node + ", "
            elif color[node] == "black":
                cross = cross +  root + "->" + node+ ", "
    print visit
    print "back: ", back.rstrip(", ")
    print "cross ", cross.rstrip(", ")


if __name__ == "__main__":
    bfs()

'''
There is no forward edge possible in BFS because all of the nodes are explored
at a level before reaching to the next level. So there's no possibility that
a node at a lower tries to explore a node at a higher level.  
'''
