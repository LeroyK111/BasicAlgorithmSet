#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 我们导入机器学习包
from sklearn.neighbors import KNeighborsClassifier

# 构造数据集
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]

# 实例化一个训练模型
# n邻居数量，查询默认使用邻居数
estimator = KNeighborsClassifier(n_neighbors=2)

# 调用对应的方法
estimator.fit(x, y)

# 预测一下其他值
ret = estimator.predict([[0]])
# 属于哪个类别
print(ret)
