import heapq

graph = {
    "S": {"A": 1, "C": 4, "D": 5},
    "A": {"C": 2,},
    "C": {"D": 5},
    "D": {"C": 5}
}

H = {
    "S": 7,
    "A": 6,
    "C": 2,
    "D": 1,
    "G": 0
}

def a_star(graph, H, start, goal):
    pq = [(H[start], 0, start, [start])]
    vis = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in vis:
            continue
        vis.add(node)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        for neighbor, w in graph[node].items():
            if neighbor not in vis:
                new_g = g + w
                new_f = new_g + H[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

# Run A* from S to C
a_star(graph, H, "S", "C")