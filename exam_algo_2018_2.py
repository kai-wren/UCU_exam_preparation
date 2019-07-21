class Node:
    def __init__(self, value, parent=None):
        self.v = value
        self.l = None
        self.r = None
        self.p = parent

    def insert(self, value):
        if self.v:
            if value < self.v:
                if self.l is None:
                    self.l = Node(value, self)
                else:
                    self.l.insert(value)
            elif value > self.v:
                if self.r is None:
                    self.r = Node(value, self)
                else:
                    self.r.insert(value)
        else:
            self.data = value
    
    def badInsert(self, value):
        if self.v:
            if value < self.v:
                if self.r is None:
                    self.r = Node(value, self)
                else:
                    self.r.badInsert(value)
            elif value > self.v:
                if self.l is None:
                    self.l = Node(value, self)
                else:
                    self.l.badInsert(value)
        else:
            self.data = value

    def PrintTree(self):
        if self.l:
            self.l.PrintTree()
        print(self.v),
        if self.r:
            self.r.PrintTree()

    def left(self):
        return self.l

    def right(self):
        return self.r

    def parent(self):
        return self.p

    def value(self):
        return self.v


def fillTree():
    tree = Node(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(15)
    tree.insert(30)
    # tree.badInsert(10)
    tree.insert(80)
    tree.insert(85)
    # tree.badInsert(90)

    tree.PrintTree( )
    return tree

def IsBinarySearchTree(tree):
    resFlag = True

    left = tree.left()
    right = tree.right()
    if left:
        if left.value() > tree.value():
            resFlag = False
        else:
            resFlag = IsBinarySearchTree(left)
    
    if resFlag == False:
        return resFlag

    if right: 
        if right.value() < tree.value():
            resFlag = False
        else:
            resFlag = IsBinarySearchTree(right)

    return resFlag

T = fillTree()
result = IsBinarySearchTree(T)
print(result)
