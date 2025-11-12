tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, depth, limit):
    if depth > limit:
        return
    print(node, end=" ")
    for nxt in tree[node]:
        dls(nxt, depth+1, limit)

def ids(start, max_depth):
    for limit in range(max_depth+1):
        print(f"\nDepth limit = {limit}: ", end="")
        dls(start, 0, limit)

ids('A', 3)