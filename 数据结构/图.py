#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A --- B
|   / |
| /   |
C     D


✅ 1. 按边是否有方向分：
类型	特点	示例
无向图	边没有方向，A→B 和 B→A 是一样的	好友关系、双向道路
有向图	边有方向，A→B 和 B→A 不等	关注关系、任务依赖

✅ 2. 按边是否带权重分：
类型	特点	示例
无权图	边没有权重	迷宫、社交图
带权图	每条边有一个权值（如距离、花费）	地图导航、最短路径问题

✅ 3. 按连接方式分：
类型	特点
稠密图	边多，接近于完全图
稀疏图	边少
连通图（无向）	任意两点之间有路径
强连通图（有向）	任意两点之间互相可达
弱连通图（有向）	忽略方向后连通

✅ 4. 特殊图类型：
图类型	特点/用途
树（Tree）	一种无环、连通的无向图
有向无环图（DAG）	用于表示依赖关系，如任务调度、拓扑排序
完全图	所有点之间都有边
二分图	顶点分两组，边只连接不同组的点
图的补图	没有边的地方加边

✅ 图的存储方式：
方式	优点	缺点
邻接表	节省空间，适合稀疏图	查询是否相邻较慢
邻接矩阵	查询快（O(1)），适合稠密图	空间大，O(n²)
"""
# 用字典模拟邻接表
graph = {"A": ["B", "C"], "B": ["A", "C", "D"], "C": ["A", "B"], "D": ["B"]}


# 深度优先搜索
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


dfs(graph, "A")  # 输出: A B C D （或其它顺序，取决于递归顺序）


from collections import deque


# 广度优先搜索
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, "A")  # 输出: A B C D
