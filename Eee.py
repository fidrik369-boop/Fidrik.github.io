# A* Algorithm Implementation

def a_star_algorithm(graph, start, stop):

    open_list = [start]
    closed_list = set()

    g = {start: 0}            # Cost from start node
    parents = {start: start}  # Parent tracking

    while open_list:
        n = None

        # Find node with lowest f(n) = g(n) + h(n)
        for v in open_list:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop:
            # Reconstruct path
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()

            print("Path found:", reconst_path)
            return reconst_path

        open_list.remove(n)
        closed_list.add(n)

        # Check neighbors
        for (m, weight) in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.append(m)

    print("Path does not exist!")
    return None


# Heuristic function (estimated cost to goal)
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'E': 7,
        'D': 1,
        'G': 0
    }
    return H_dist[n]


# Graph from experiment sheet
graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

# Run A*
a_star_algorithm(graph_nodes, 'A', 'G')
