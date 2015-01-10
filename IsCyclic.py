color = {"A":'white',"B":'white',"C":'white',"D":'white',"E":'white'}
iscycle = False
Path = ""
def cycle(graph, start):
    _cycle(start, graph)
    if iscycle:
        print Path
    else:
        print "ACYCLIC"

def _cycle(start, graph, path=""):
    global iscycle
    global Path
    path = path + start + "->"
    color[start] = 'gray'
    if start not in graph:
        color[start] = 'black'
        return 
    for n in graph[start]:
        if color[n] == 'white':
            _cycle(n, graph, path)
        elif color[n] == 'gray':
            Path = path+ n
            iscycle = True
            return
    color[start] = 'black'
    
        

if __name__ == "__main__":
    graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A","E"]}
    cycle(graph, "A")
    
