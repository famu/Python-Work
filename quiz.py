class tree(object):
    __slot__="node", "left","right"
    def __init__(sleft, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

def _fib(n, cache={}):
    if n in cache:
        return n
    cache[n] = 1 if n<2 else _fib(n-1, cache) + _fib(n-2,cache)
    return cache[n]

def _longest(tree):
    if tree==[]:
        return 0,-1
    left, root, right = tree
    l1,d1 = _longest(left)
    l2,d2 = _longest(right)
    return max([d1+d2+2,l1,l2]), max(d1,d2)+1
_longest = lambda tree: _longest(tree)[0]


def _qselect(index, tree):
    if tree==[]:        
        return 0, None
    left, node, right = tree
    num, x = _qselect(index, left)
    if index <= num:
        print index, num, x, node 
        return num, x
    if index == num+1:
        print index, index, x, node
        return index, node
    num2, y = _qselect(index-num-1,right)
    print index, num+num2+1, y, node
    return num+num2+1,y
def qselect(index, tree):
    return _qselect(index,tree)[i]

def qsort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]

