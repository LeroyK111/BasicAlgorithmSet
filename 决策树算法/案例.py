#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
关于泰坦尼克号的乘客生还数据
"""
import pandas as pd
import numpy as np
# 字典特征提取
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

data = pd.read_csv(r"learning\机器学习\自学算法\决策树算法\titanic.csv")
# print("基本统计函数\n", data.describe())
# print(data.columns)

# 数据基本处理
# 划分特征值和目标值
x = data[["Pclass", "Age", "Sex"]]
y = data["Survived"]

# 判断有无nan值
# print(pd.isnull(x["Pclass"]).values.any())
# print(pd.isnull(x["Age"]).values.any())
# print(pd.isnull(x["Sex"]).values.any())
# print(pd.isnull(y).values.any())

# 缺失值处理
x["Age"].fillna(x["Age"].mean(), inplace=True)

# 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

# 特征工程
transfer = DictVectorizer()
x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
x_test = transfer.fit_transform(x_test.to_dict(orient="records"))

# 机器学习，决策树模型
# 这里需要初始剪枝
# estimator = DecisionTreeClassifier(criterion="entropy", max_depth=5)
estimator = DecisionTreeClassifier()
estimator.fit(x_train, y_train)

# 模型评估
y_pre = estimator.predict(x_test)
print("预测值\n", y_pre)

# 准确率
score = estimator.score(x_test, y_test)
print("准确率:\n", score)

# 存储决策树
export_graphviz(estimator, out_file=r"learning\机器学习\自学算法\决策树算法\tree.dot")