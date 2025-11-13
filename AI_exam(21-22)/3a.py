import numpy as np

web = ['w1', 'w2', 'w3', 'w4', 'w6']
links = {
    'w1': ['w2', 'w4'],
    'w2': ['w3', 'w4'],
    'w3': ['w2', 'w1', 'w6'],
    'w4': ['w6'],
    'w6': ['w4'],
}

n = len(web)
adj_matrix = np.zeros((n, n))

for i, src in enumerate(web):
    for dst in links.get(src, []):
        j = web.index(dst)
        adj_matrix[j][i] = 1 


for i in range(n):
    col_sum = np.sum(adj_matrix[:, i])
    if col_sum != 0:
        adj_matrix[:, i] /= col_sum
    else:
        adj_matrix[:, i] = 1 / n

def pagerank(M, num_iterations=100, d=0.85):
    N = M.shape[0]
    rank = np.ones(N) / N
    for _ in range(num_iterations):
        rank = (1 - d) / N + d * M @ rank
    return rank

ranks = pagerank(adj_matrix)
for i, site in enumerate(web):
    print(f"PageRank of {site}: {ranks[i]:.4f}")