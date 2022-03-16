from stack import Stack
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../Week 2')


class Graph:
    def __init__(self, V=None, E=None, directed=True):
        self.gdict = {}
        self.directed = directed
        if V and E:
            self.addVertices(V)
            self.addEdges(E)

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        edges = []
        for key, value in self.gdict.items():
            for edge in value:
                edges.append((key, edge))
            # pair key with each element in the value
            # add each pair into edges
        return edges

    def addVertices(self, vertices):
        if type(vertices) != list:
            vertices = [vertices]
        for v in vertices:
            if v not in self.gdict:
                self.gdict[v] = []

    def addEdges(self, edges):
        for sv, ev in edges:
            if sv not in self.gdict:
                self.addVertices(sv)
            if ev not in self.gdict:
                self.addVertices(ev)
                # Directed graph
            if self.directed:
                if ev not in self.gdict[sv]:
                    self.gdict[sv].append(ev)
            else:
                if ev not in self.gdict[sv]:
                    self.gdict[sv].append(ev)
                if sv not in self.gdict[ev]:
                    self.gdict[ev].append(sv)


g = Graph(['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b')])
# output:  {'a': ['b'], 'b': ['c'], 'c': ['a', 'b']}
g = Graph(['a', 'b', 'c'], [('a', 'b'), ('b', 'c'),
          ('c', 'a'), ('c', 'b')], False)
# output:  {'a': ['b', ‘c’], 'b': [‘a’, 'c'], 'c': ['b',’a’]}
# print(g.getEdges())

g.addVertices("233")
# print(g.getVertices())
g.addEdges([("d", "e"), ("d", "c")])
# print(g.getEdges())


class GraphWeight(Graph):
    def addEdges(self, edges):
        for sv, ev, weight in edges:
            if sv not in self.gdict:
                self.addVertices(sv)
            if ev not in self.gdict:
                self.addVertices(ev)
                # Directed graph
            if self.directed:
                if ev not in self.gdict[sv]:
                    self.gdict[sv].append((ev, weight))
            else:
                if ev not in self.gdict[sv]:
                    self.gdict[sv].append((ev, weight))
                if sv not in self.gdict[ev]:
                    self.gdict[ev].append((sv, weight))

    def depthFirstSearch(self, start, goal):
        current = start
        visited = []
        toVisit = Stack()
        toVisit.push(current)

        while toVisit.isEmpty():
            current = toVisit.pop()
            if current == goal:
                visited.append(current)
                # add the current into the visited list
                break
            else:
                # each adjacent vertices of the current vertex
                for v in [v for v, weight in self.gdict[current]]:
                    # the unvisited vertex can be pushed into the stack
                    print(current)
                    if current not in visited:
                        visited.append(current)

        return visited

    def breadthFirstSearch(self, start, goal):
        current = start
        visited = []
        toVisit = Queue()
        toVisit.enqueue(current)

        while toVisit is not empty:
            current = toVisit.dequeue()
            if current == goal:
                add the current into the visited list
                break
            else:
                # each adjacent vertices of the current vertex
        for v in [v for v, weight in self.gdict[current]]:
                    the unvisited vertex can be pushed into the stack
                if current not be visited, add it into the visited list
        
        return visited


g = GraphWeight(["a", "b", "c"], [("a", "b", 1),
                ("b", "c", 2), ("c", "a", 3)], True)
# print(g.getEdges())
print(g.depthFirstSearch("a", "c"))
