import sys
import heapq
 

def median(list):
    result = []
    minheap =[]
    maxheap = []
    median = 0
    for k in list:
        if k >= median:
            heapq.heappush(minheap,k)
        else:
            heapq.heappush(maxheap,k)
            heapq._heapify_max(maxheap)
        minl = len(minheap)
        maxl = len(maxheap)
        if minl == maxl:
            median = (minheap[0] + maxheap[0])/2.0
        elif abs(minl - maxl) == 1:
            if minl>maxl:
                median = minheap[0]
            else:
                median = maxheap[0]
        elif minl - maxl > 1:
            while minl - maxl >1:
                heapq.heappush(maxheap, heapq.heappop(minheap))
                heapq._heapify_max(maxheap)
                minl = len(minheap)
                maxl = len(maxheap)
            if minl == maxl:
                median = (minheap[0] + maxheap[0])/2.0
            elif minl>maxl:
                median = minheap[0]
            else:
                median = maxheap[0]
        else: # if maxl - minl > 1:
            while maxl - minl > 1:
                heapq.heappush(minheap, heapq.heappop(maxheap))
                minl = len(minheap)
                maxl = len(maxheap)
            if minl == maxl and minl !=0:
                median = (minheap[0] + maxheap[0])/2.0
            elif minl>maxl:
                median = minheap[0]
            else:
                median = maxheap[0]
        result.append(median)
        
    print result

if __name__ == '__main__':
    median([5,3,4,1,6])
