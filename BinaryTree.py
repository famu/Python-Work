class Tree:
        def __init__(self, root, left = None, right = None):
                self.root = root
                self.left = left
                self.right = right
               

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

      
def find(t, x):
    mini = 10000.0 # first time it is big enough
    diff= set()
    return _find(t, x, mini,diff)

def _find(t, x, mini, diff):
    if t is None:
        return min(diff)
    if t.root > x:
        diff.add(abs(t.root - x))
        return _find(t.left, x, mini,diff)
    if t.root < x:
        diff.add(abs(x - t.root))    
        return _find(t.right, x, mini,diff)
    
    
def postorder(pre, inor):    
    root = pre[0]
    lst = inor[:inor.index(root)]
    rst = inor[inor.index(root)+1:]
    print lst, rst[::-1], root
    

    

t = Tree(5, Tree(3, Tree(2), Tree(4)), Tree(7, Tree(6), Tree(8)))
print(find(t,6.7))
    
#postorder([1,2,3,5], [2,1,3,5])
