from queue import PriorityQueue

# Number of vertices
v = 14
graph = [[] for i in range(v)]

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def best_first_search(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source))
    visited[source] = True

    print("Path:", end=" ")
    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ")

        if u == target:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))

# Example Graph Construction
add_edge(0, 1, 3)
add_edge(0, 2, 6)
add_edge(1, 4, 9)
add_edge(1, 5, 8)
add_edge(2, 7, 14)
add_edge(3, 6, 7)
add_edge(8, 10, 6)
add_edge(9, 11, 1)
add_edge(0, 3, 5)
add_edge(2, 6, 12)
add_edge(8, 9, 5)
add_edge(9, 12, 10)
add_edge(9, 13, 2)

# Run Best First Search
best_first_search(0, 9, v)
