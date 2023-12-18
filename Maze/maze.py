import sys
class Node:
    def __init__(self,state,parent,acton):
        self.state = state
        self.acton = acton
        self.parent = parent
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
        
    def addFrontier(self, node):
        self.frontier.append(node)
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
        # with open(filename) as f:
        #     contents = f.read()
        # print(contents)
        
        # contents = contents.splitlines()
        # self.height = len(contents)
        # self.width = max(len(line) for line in contents)
        # print(self.height, self.width)
        
        # 2nd way of calculating height and width from file contents
        file = open(filename,'r')
        lines = file.readlines()
        if not ("A" in " ".join(lines)):
            raise Exception("maze must have exactly one start point")
        if not ("B" in " ".join(lines)):
            raise Exception("maze must have exactly one End point")
        
        # self.height = max([i+1 for i in range(len(lines))])
        self.height = len(lines)
        self.width = max([len(line)-1 for line in lines])
            
        self.wall = []
        for i in range(self.height):
            row=[]
            for j in range(self.width):
                try:
                    if lines[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    if lines[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    if lines[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.wall.append(row)
        self.solution = None
        
    def solve(self):
        start = Node(state = self.start,parent = None, action = None)
        frontier = StackFrontier()
        frontier.addFrontier(start)
        
        self.iteration = 0
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("No solution.")
            else:
                node = frontier.remove()
                self.iteration += 1
                if node.state == self.goal:
                    actions = []
                    cells = []
                    while self.parent is not None:
                        actions.append(node.action)
                        cells.append(node.action)
                        node = node.parent
                    actions.reverse()
                    cells.reverse()
                    self.solution = (actions, cells)
                    return 
                self.explored.add(node)
        
        
        
        
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])