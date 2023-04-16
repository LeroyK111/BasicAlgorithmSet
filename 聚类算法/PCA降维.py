#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.decomposition import PCA

data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]

# 保留多少维度
transfer = PCA(n_components=2)
trans_data = transfer.fit_transform(data)
print(trans_data)

# 保留多少信息
transfer = PCA(n_components=.9)
trans_data = transfer.fit_transform(data)
print(trans_data)