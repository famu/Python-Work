import random,time, heapq
#O(n^2)
def nbesta(a,b):
    t = time.time()
    AxB = []
    for i in a:
        for j in b:
            check = False
            for x, (aa, bb) in enumerate(AxB):
                if aa+bb > i+j:
                        AxB.insert(x, (i,j))
                        check = True
                        break
                elif aa+bb == i+j:
                        AxB.insert(x, (i,j))
                        check = True
                        break
            if check == False:
                AxB.append((i,j))
    print time.time() - t   # time elapsed, in seconds5
    return AxB[:len(a)]

#O(n^2)
def nbestb(a,b):
    t = time.time()
    AxB = [(i+j,i,j) for i in a for j in b]
    n = qselect(len(a)+2,AxB)
    AxB = [(i,j) for (t, i, j) in AxB if t < n[0]]
    print time.time() - t   # time elapsed, in seconds5
    return sorted(AxB, key=lambda k:(k[0]+k[1],k[1]))


#O(n)
def nbestc(a,b):
    t = time.time()
    AxB = []
    for i in a:
        for j in b:
            heapq.heappush(AxB,(i+j,j,i))
    sorted = []
    for i in range(len(a)):
        sum,i,j = heapq.heappop(AxB)
        sorted.append((i,j))
    print time.time() - t   # time elapsed, in seconds5
    return sorted



def qselect(k, list):
    if list == None:
        return None
    pivot = random.randint(0, len(list)-1)
    rest = list[:pivot] + list[pivot+1:]
    left = [x for x in rest if x < list[pivot]]
    left_size = len(left)
    if k == left_size+1:
        return list[pivot]
    elif k <= left_size: 
        return qselect(k, left)
    else:
        right = [x for x in rest if x >= list[pivot]]
    return qselect(k - left_size -1 , right)
