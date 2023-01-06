from collections import deque

# I'm gonna be honest, I have no clue what most of this does or how it works
# This is one of the times where I just have to thank stack overflow for existing
class Pathfinding():
    def __init__(self,GAME):
        self.game = GAME
        self.map = GAME.map.levelMap
        self.paths = [-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]
        self.graph = {}
        for y,row in enumerate(self.map):
            for x,column in enumerate(row):
                if column == "0": self.graph[(x,y)] = self.graph.get((x,y),[])+[(x+dx,y+dy) for dx,dy in self.paths if (x+dx,y+dy) not in self.game.map.worldMap]
        
    def search(self,START,GOAL,GRAPH):
        queue = deque([START])
        visited = {START:None}

        while queue:
            currentNode = queue.popleft()
            if currentNode == GOAL: break
            nextNodes = GRAPH[currentNode]

            for nextNode in nextNodes:
                if nextNode not in visited:
                    queue.append(nextNode)
                    visited[nextNode] = currentNode
        return visited
    
    def getPath(self,START,GOAL):
        self.visited =self.search(START,GOAL,self.graph)
        path = [GOAL]
        step = self.visited.get(GOAL,START)

        while step and step != START:
            path.append(step)
            step = self.visited[step]
        return path[-1]