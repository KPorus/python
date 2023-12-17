class Node:
    def __init__(self,state,parent,acton):
        self.state = state
        self.acton = acton
        self.parent = parent
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("Frontier is empty")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node