#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# 这是斑点数据，属于小数据集
from sklearn.datasets._samples_generator import make_blobs
# 算法
from sklearn.cluster import KMeans
# 评估模型
from sklearn.metrics import calinski_harabasz_score
"""
x为样本特征
y为样本类别
"""
x, y = make_blobs(
    # 样本数量
    n_samples=1000,
    # 返回两个特征
    n_features=2,
    # 簇中心，所在位置
    centers=[
        [-1, -1],
        [0, 0],
        [1, 1],
        [2, 2],
    ],
    # 簇方差
    cluster_std=[.4, .2, .2, .2],
    # 随机数种子
    random_state=9)

# print(X.shape)
# print(y.shape)

# 画个图
# plt.scatter(x[:, 0], x[:, 1])
# plt.pause(5)

# !现在我们就看一看，使用k-meanss进行聚类计算，使用ch方法评估
y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(x)

# 查看聚类效果
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.pause(5)

# ch评估分数越高越好
print(calinski_harabasz_score(x, y_pred))
