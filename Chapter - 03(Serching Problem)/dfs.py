tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
vis = set()      
def dfs(node):
    if node not in vis:
        print(node, end=" ")
        vis.add(node)
        for next in tree[node]:
            dfs(next)
    
dfs('A')