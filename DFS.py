color = {"A":'white',"B":'white',"C":'white',"D":'white',"E":'white'}
timestamp = {"A":0,"B":0,"C":0,"D":0,"E":0}
time = 0
def dfs(start, spaces, graph):
    color[start] = 'gray'
    global time
    timestamp[start] = time;
    time+=1
    if start not in graph:
        color[start] = 'black'
        return 
    for n in graph[start]:
        if color[n] == 'white':
            print '     '*spaces, start,"->",n
            dfs(n, spaces+1, graph)
        elif color[n] == 'gray':
            print '     '*spaces, " *"+ start,"->",n,"(back)"
        elif timestamp[n] < timestamp[start]:
            print '     '*spaces, " *"+ start,"->",n,"(cross)"
        else:
            print '     '*spaces, " *"+ start,"->",n,"(forward)"
    color[start] = 'black'
    return



if __name__ == "__main__":
    graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"], "E":[]}
    dfs("A", 0, graph)

