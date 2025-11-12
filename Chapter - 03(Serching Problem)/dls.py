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
    for next in tree[node]:
        dls(next, depth + 1, limit)

dls('A', 0, 3)