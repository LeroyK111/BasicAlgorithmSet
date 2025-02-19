import numpy as np

"""
链接分析算法广泛应用于 搜索引擎排名（如 Google PageRank）、社交网络分析、推荐系统 等领域。最著名的链接分析算法包括：

PageRank（网页排名）
HITS（Hyperlink-Induced Topic Search）（主题搜索）
SALSA（Stochastic Approach for Link-Structure Analysis）
"""


def pagerank(G, alpha=0.85, max_iter=100, tol=1.0e-6):
    N = len(G)
    M = np.array(G, dtype=float)  # 邻接矩阵
    M /= M.sum(axis=0)  # 归一化，使列和为 1

    rank = np.ones(N) / N  # 初始 PageRank 值
    teleport = np.ones(N) / N  # 随机跳转概率

    for _ in range(max_iter):
        new_rank = alpha * np.dot(M, rank) + (1 - alpha) * teleport
        if np.linalg.norm(new_rank - rank, ord=1) < tol:
            break  # 收敛
        rank = new_rank

    return rank


# 定义网页链接关系（邻接矩阵）
G = [
    [0, 0, 1, 0],  # A -> C
    [1, 0, 0, 1],  # B -> A, D
    [0, 1, 0, 1],  # C -> B, D
    [0, 0, 1, 0],  # D -> C
]

ranks = pagerank(G)
print("网页排名（PageRank）:", ranks)
