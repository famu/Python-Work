
class Tree:
        def __init__(self, root=None):
                self.root = root
                self.left = None
                self.right = None
                self.counter = 0

        def insert(self, value):
                if value < self.root:
                        if self.left is None:
                                self.left = Tree(value)
                        else:
                                self.left.insert(value)
                else:
                        if self.right is None:
                                self.right = Tree(value)
                        else:
                                self.right.insert(value)

        def search(self, value):
                print self
                if value < self.root:
                        if self.left is None:
                                return False
                        return self.left.search(value)
                elif value > self.root:
                        if self.right is None:
                                return False
                        return self.right.search(value)
                else:
                        return True

        def delete(self, value):
                #print self
                #print self.root
                if value < self.root:
                        if self.left is not None:
                            self.left.delete(value)
                elif value > self.root:
                        if self.right is not None:
                            self.right.delete(value)
                elif value == self.root:
                    rml = self.left                    
                    while(rml.right != None):
                        rml = rml.right    
                    self.root = rml.root
                    rml.root = None

                
        #for testing but is not used   
        def rl(self):
            print self
            if self.right != None:                
                self.right.rl()
            else:
                #print self                
                return self

        #for testing but is not used    
        def ll(self):
            print self
            if self.left != None:                
                self.left.ll()
            else:
                #print self                
                return self
            
        

        def preOrder(self):
            print self.root
            if self.left != None:
                self.left.preOrder()
            if self.right != None:
                self.right.preOrder()
                
        def postOrder(self):            
            print self.root
            if self.right != None:
                self.right.postOrder()
            if self.left != None:    
                self.left.postOrder()

        def inOrder(self):            
            if self.left != None:
                self.left.inOrder()
            print self.root
            if self.right != None:
                self.right.inOrder()


def qsort(a):
        if a == []:
                return []
        else:
                pivot = a[0]
                left = [x for x in a if x < pivot ]
                right = [x for x in a[1:] if x >= pivot]
                return [qsort(left)] + [pivot] + [qsort(right)]

'''
mergsort divides array into subarrays
'''

def mergesort(list):
    if len(list)<=1:
        return list
    middle=len(list)/2
    left =list[:middle]
    right=list[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    "print res"
    return res
'''
merg function merges the arrays in such that elements are sorted in new array
'''

def merge(left,right):
    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res




#not working
def plot(t, lvl, offset, ref, arr):
        if t != []:
                arr[lvl][offset] = t.root
                #print t.root
                if t.left != []:                        
                        arr[lvl+1][offset-ref/2] = "/"
                        plot(t.left, lvl+2, offset - ref, ref/2, arr)
                if t.right != []:
                   arr[lvl+1][offset+ref/2] = "\\"
                   plot(t.right, lvl+2, offset+ref, ref/2, arr)
           
                        

        
        
        
'''
how to run


>>> exec('''
t = Tree(9)
t.insert(5)
t.insert(15)
t.insert(3)
t.insert(7)
t.insert(13)
t.insert(18)
t.insert(8)
''')


>>> t.root
9
>>> t.delete(9)
>>> t.root
8
>>> t.search(9)
False
>>> t.search(8)
True



'''




