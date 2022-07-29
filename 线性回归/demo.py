#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
import numpy as np

# 我们自己构造数据，做线性回归

x = np.random.randint(1, 100, (8, 2))
y = np.random.randint(800, 1000, (8)) / 10

# 实例化模型
estimator = LinearRegression()
estimator.fit(x, y)

# 查看一下系数
coef = estimator.coef_
print("我的系数是", coef)

# 预测一下
print("预测值是", estimator.predict([[80, 100]]))
