graph = {"cs10": ["cs20", "cs11"], "cs11": ["cs21"], "cs20": ["cs30"], "cs21":["cs20", "cs12"], "cs12":["cs30"], "cs30":[]}
def dfs_topolgical_sort(graph,start):
    path = ""
    stack = [start]
    length = len(graph)
    cache = {}  
    while stack != []:
        for element in stack:
            if element not in cache:
                cache[element] = length
                length = length - 1

        node = stack.pop()
        if node not in path: 
            path = path + " -> " + node
        else:
            print "no topological order"
            return
        for n in reversed(graph[node]): 
            if n not in path and not n in stack:
                stack.append(n)
    print path.lstrip(" -> ")
    

if __name__ == "__main__":
    dfs_topolgical_sort(graph, "cs10")

