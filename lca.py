class Tree(object):
    def __init__(sleft, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right
        parent = Tree(n)
        
#inserts in place if value doens't already exist. otherwise doesn nothing
def insert(t, value):
                if value < t and value != t:
                        if t.left is None:
                                t.left = Tree(value)
                        else:
                                insert(t.left, value)
                else:
                        if t.right is None:
                                t.right = Tree(value)
                        else:
                                insert(t.right,value)
        


def lca(tree, x,y):
    if tree is None:
        return false, false, None, -1
    fl1, fl2, lcal, lenl = lca(tree.left, x,y)
    if fl1 and fl2:
        return fl1, fl2, lcal, lenl
    fr1, fr2, lcar, lenr = lca(tree.right,x,y)
    if fr1 and fr2:
        return fr1, fr2, lcar, lenr
    if not fl1 and not fl2:
        return F,F,N,-1
    if fl1 and fr2:
        return t,t
    


def lca(node, n1, n2):
  if match(node.left, n1) and match(node.left, n2):
    return lca(node.left, n1, n2) # until we find the least common ancestor by node.left
  if match(node.right, n1) and match(node.right, n2):
    return lca(node.right, n1, n2) # until we find the least common ancestor by node.right
  return node
  
def match(node, n):
  if node is None: return False
  if node == n: return True
  return match(node.left) or match(node.rigth)


'''
('''
t = Tree
insert(t,5)
insert(t,15)
insert(t,3)
insert(t,7)
insert(t,13)
insert(t,18)
insert(t,8)
insert(t,4)
''')
'''
