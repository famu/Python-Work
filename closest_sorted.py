
def kclosest_sorted(A,k,x):
    newA = [abs(i-x) for i in A]
    
    minIndex = 0;
    for i in xrange(len(newA)):
        if newA[minIndex] > newA[i]:
            minIndex = i
    left = minIndex -1
    right = minIndex +1
    result = [A[minIndex]]    
    for j in xrange(k-1):
        if abs(A[left]-A[minIndex]) < abs(A[minIndex]-A[right]):
            result.append(A[left])
            left -=1
        else:
            result.append(A[right])
            right +=1
            
    print result
    
if __name__ == "__main__":
    A = [1,5,7,8,9,12,14,17,19,23,34]
    kclosest_sorted(A,4,10)
