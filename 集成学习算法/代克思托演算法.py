import heapq


def dijkstra(graph, start):
    # 初始化：距离表、优先队列
    shortest_distances = {node: float("inf") for node in graph}
    shortest_distances[start] = 0
    priority_queue = [(0, start)]  # (距离, 节点)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前节点的距离已经超过记录的最短路径，则跳过
        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 如果找到更短的路径，则更新距离
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


# 创建加权图（邻接表）
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

# 计算从 A 到所有节点的最短路径
shortest_paths = dijkstra(graph, "A")
print("最短路径:", shortest_paths)
