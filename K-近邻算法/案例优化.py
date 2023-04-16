#!/usr/bin/python
# -*- coding: utf-8 -*-
# 数据集
from sklearn.datasets import load_iris
# 标准化
from sklearn.preprocessing import StandardScaler
# 数据分割
from sklearn.model_selection import train_test_split, GridSearchCV
# knn算法
from sklearn.neighbors import KNeighborsClassifier
"""
1.获取数据集
2.数据基本处理
3.特征工程
4.机器学习（模型训练）
5.模型评估
"""
iris = load_iris()

# 不需要数据清洗，只需要分割数据
# train训练，test测试
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=.2, random_state=22)

# 特征工程
transfer = StandardScaler()
# 标准化（无量纲）
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 开始训练(给个节点数)
estimator = KNeighborsClassifier(n_neighbors=1)
# 加入优化措施，交叉网络搜索
param_grid = {"n_neighbors": [1, 3, 5, 7, 9]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=10, n_jobs=-1)

estimator.fit(x_train, y_train)

# 模型评估
# 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是:", y_pre)
print("预测值和真实值对比:", y_pre == y_test)

# 输出准确率
ret = estimator.score(x_test, y_test)
print("准确率:", ret)

# 其他评价指标
print("最好的模型", estimator.best_estimator_)
print("最好的结果", estimator.best_score_)
print("整体模型结果", estimator.cv_results_)
