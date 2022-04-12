

class Solution:

    def find(self, start, end, visited, path):
        if visited[start]:
            return

        if end == start:
            self.pathes.append(path[:])


        visited[start] = 1
        for v in self.graph[start]:
            path.append(v)
            self.find(v, end, visited, path)
            path.pop()

        visited[start] = 0

        return


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.pathes = []
        self.graph = graph
        visited = [0 for i in range(len(graph))]
        self.find(0, len(graph) - 1, visited, [0])

        return self.pathes
