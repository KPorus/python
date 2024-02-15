import sys
class Node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action
        
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
        self.points = []
        startP = {}
        endP = {}
        for i in range(self.height):
            row=[]
            point = []
            for j in range(self.width):
                try:
                    if lines[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    if lines[i][j] == "B":
                        self.goal = (i, j)
                        endP["x"] = i
                        endP["y"] = j
                        row.append(False)
                    if lines[i][j] == " ":
                        row.append(False)
                        point.append(abs((endP['x'] - i) + (endP['y'] - j)))
                        print(point)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.wall.append(row)
            self.points.append(point)
            #print(self.points)
        self.solution = None
    
    def neighbors(self,state):
        row, col = state
        candidates = [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1))
        ]

        
        result = []
        for action, (r,c) in candidates:
            if 0<=r < self.height and 0<=c < self.width and not self.wall[r][c]:
                result.append((action,(r,c)))
        return result
    
    def solve(self):
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.addFrontier(start)

        self.iteration = 0
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("No solution.")

            node = frontier.remove()
            self.iteration += 1
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.addFrontier(child)

        
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.wall):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()    
        
        
        
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.iteration)
print("States Explored:", m.explored)
print("Solution:")
m.print()