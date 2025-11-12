from collections import deque
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(tree, start):
    vis = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in vis:
            print(node, end=" ")
            vis.add(node)
            
            for neighbor in tree[node]:
                if neighbor not in vis:
                    q.append(neighbor)

bfs(tree, 'A')