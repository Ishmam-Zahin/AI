from DFS_BFS import BFS_DFS
from Set import Set

class A_Star_Search(BFS_DFS):
    def __init__(self):
        super().__init__()
    
    def herioustic(self, state):
        i, j, step = state
        ei, ej, step2 = self.end
        h = abs(ei - i) + (ej - j)

        return h
    
    def getStep(self, state):
        i, j, step = state

        return step
    
    def solve(self):
        s = Set()
        s.insert((self.herioustic(self.start) + self.getStep(self.start), self.start))
        self.parent[self.start] = None

        while s.begin():
            h, parent = s.begin().value
            pi, pj, step = parent
            self.num_explored += 1
            s.delete(node = s.begin())

            if self.maze[pi][pj] != "A" and self.maze[pi][pj] != "B":
                self.maze[pi][pj] = 2

            if self.maze[pi][pj] == "B":
                self.markPath()
                break

            for neighbour in self.getNeighbours(parent):
                s.insert((self.herioustic(neighbour) + self.getStep(neighbour), neighbour))



def main():
    obj = A_Star_Search()
    obj.print()
    print()
    print("SOLVING...")
    obj.solve()
    print("Number of state explored: ", obj.num_explored)
    print()
    obj.print(showExplored = True)
    print()




if __name__ == "__main__":
    main()