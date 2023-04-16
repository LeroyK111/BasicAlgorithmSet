#!/usr/bin/python
# -*- coding: utf-8 -*-

# 归一化处理(无量纲)
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

df = pd.DataFrame({
    "milage": [1000, 500, 100],
    "Liters": [7.12123, 8.3123214, 9.23132],
    "consumtime": [1.21323, .9, .2],
    "target": [3, 2, 1]
})
"""
归一化，只适合传统精确小数据场景
"""
# 归一化，无量纲处理
# transfer = MinMaxScaler(feature_range=(0, 1))
# 调用fit_transfrom方法
# minmax_data = transfer.fit_transform(df[["milage", "Liters", "consumtime"]])
# 量纲统一后
# print(minmax_data)
"""
标准化
1.异常值对我影响很小
2.适合嘈杂的大数据环境
"""
transfer = StandardScaler()
minmax_data = transfer.fit_transform(df[["milage", "Liters", "consumtime"]])
print(minmax_data)
