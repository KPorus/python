import sys
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
        
class Maze():
    def __init__(self,filename):
        print(sys.argv[1])
        
        # first way of calculating height and width from file contents
        with open(filename) as f:
            contents = f.read()
        print(contents)
        
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        print(self.height, self.width)
        
        # 2nd way of calculating height and width from file contents
        file = open(filename,'r')
        lines = file.readlines()
        print(lines)
        if not ("A" in " ".join(lines)):
            raise Exception("maze must have exactly one start point")
        if not ("B" in " ".join(lines)):
            raise Exception("maze must have exactly one End point")
        
        # self.height = max([i+1 for i in range(len(lines))])
        self.height = len(lines)
        self.width = max([len(line)-1 for line in lines])
        print(self.height, self.width)
        pass

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])