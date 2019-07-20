class stack:
    
    def __init__(self):
        self.stack_data=[]

    def addToStack(self, new_element):
        self.stack_data.append(new_element)

    def retrieveFromStack(self):
        self.stack_data.pop()
        
    def showStack_content(self):
        print(self.stack_data)

stack = stack()

stack.addToStack('A')
stack.addToStack('B')
stack.addToStack('C')
stack.showStack_content()
stack.retrieveFromStack()
stack.showStack_content()
stack.retrieveFromStack()
stack.showStack_content()
stack.retrieveFromStack()
