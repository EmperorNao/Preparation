
#
# def print_matr(matr):
#
#     out = []
#     for row in matr:
#         out.append(" ".join(list(map(str, row))))
#
#     print("\n".join(out))
#
#
# class pair:
#
#     def __init__(self, x_ = 0, y_ = 0):
#         self.x = x_
#         self.y = y_
#
#     def __add__(self, p):
#         return pair(self.x + p.x, self.y + p.y)
#
#
# class Solution:
#
#     def is_valid(self, p):
#         return 0 <= p.x < self.n and 0 <= p.y < self.n
#
#
#     def bfs(self, grid):
#
#         if grid[0][0] == 1:
#             return -1
#
#         oper = [
#             pair(-1, -1),
#             pair(-1, 0),
#             pair(0, -1),
#             pair(1, 1),
#             pair(-1, 1),
#             pair(1, -1),
#             pair(0, 1),
#             pair(1, 0)
#         ]
#
#
#         q = [pair(0, 0)]
#
#         visited = [[False for i in range(self.n)] for j in range(self.n)]
#         visited[0][0] = True
#         d = [[0 for i in range(self.n)] for j in range(self.n)]
#         p= [[pair(-1, -1) for i in range(self.n)] for j in range(self.n)]
#
#         p[0][0] = pair(-1, -1)
#
#         while q:
#             node = q.pop(0)
#
#             for op in oper:
#                 child = node + op
#                 if (self.is_valid(child) and grid[child.x][child.y] == 0 and not visited[child.x][child.y]):
#                      visited[child.x][child.y] = True
#                      q.append(child)
#                      d[child.x][child.y] = d[node.x][node.y] + 1
#                      p[child.x][child.y] = node
#
#         if not visited[self.n - 1][self.n - 1]:
#             return -1
#         path = []
#
#         node = pair(self.n - 1, self.n - 1)
#         while node.x != -1 and node.y != -1:
#             print(node.x, node.y)
#             path.append(node)
#             node = p[node.x][node.y]
#
#         return len(path)
#
#     def shortestPathBinaryMatrix(self, grid) -> int:
#
#         self.n = len(grid)
#         return self.bfs(grid)







class pair:

    def __init__(self, x_ = 0, y_ = 0):
        self.x = x_
        self.y = y_

    def __add__(self, p):
        return pair(self.x + p.x, self.y + p.y)


class Solution:

    def is_valid(self, p):
        return 0 <= p.x < self.n and 0 <= p.y < self.n


    def bfs(self, grid):

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        oper = [
            pair(-1, -1),
            pair(-1, 0),
            pair(0, -1),
            pair(1, 1),
            pair(-1, 1),
            pair(1, -1),
            pair(0, 1),
            pair(1, 0)
        ]


        q = [[1, pair(0, 0)]]

        d = [[self.n * self.n + 1 for i in range(self.n)] for j in range(self.n)]
        d[0][0] = 1

        while q:
            dist, node = q.pop(0)

            for op in oper:
                child = node + op
                x, y = child.x, child.y
                if (self.is_valid(child) and grid[x][y] == 0):
                    if dist + 1 < d[x][y]:
                        d[x][y] = dist + 1
                        q.append([d[x][y], child])

        return d[-1][-1] if d[-1][-1] <= self.n * self.n else -1

    def shortestPathBinaryMatrix(self, grid) -> int:

        self.n = len(grid)
        return self.bfs(grid)



print(Solution().shortestPathBinaryMatrix(
[
[0,0,0,0,1,1],
[0,1,0,0,1,0],
[1,1,0,1,0,0],
[0,1,0,0,1,1],
[0,1,0,0,0,1],
[0,0,1,0,0,0]
]))
