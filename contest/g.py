

class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def find_path(start, dest, d, k, cities, path):

    if path[start][dest] != -1:
        return path[start][dest]

    min_len = len(d) + 1
    add_cities = cities.copy()
    for c in cities:
        if d[start][c] <= k:
            add_cities.remove(c)
            new_path = find_path(c, dest, d, k, add_cities, path) + 1
            add_cities.add(c)
            if new_path <= min_len:
                min_len = new_path

    path[start][dest] = min_len

    return path[start][dest]


n = int(input())

distances = [[ 0 for i in range(n)] for j in range(n)]

//path_matrix = [[ 0 if i == j else - 1 for i in range(n)] for j in range(n)]

cities = []

for c in range(n):
    cities.append(point(*list(map(int, input().split(" ")))))

for i in range(n):
    for j in range(n):
        distances[i][j] = dist(cities[i], cities[j])

k = int(input())
spl = list(map(int, input().split(" ")))
start = spl[0]
dest = spl[1]


cities_set = {i for i in range(n)}
cities_set.remove(start - 1)

min_len = find_path(start - 1, dest - 1, distances, k, cities_set, path_matrix)

if min_len > len(distances):
    min_len = -1

print(min_len)
