#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer
# 计算多个树，然后取多数为真
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv(r"learning\机器学习\自学算法\决策树算法\titanic.csv")

x = data[["Pclass", "Age", "Sex"]]
y = data["Survived"]
x["Age"].fillna(x["Age"].mean(), inplace=True)

# 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

# 特征工程
transfer = DictVectorizer()
x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
x_test = transfer.fit_transform(x_test.to_dict(orient="records"))

# 换随机森林模型(先不传参数)
estimator = RandomForestClassifier()
param_grid = {
    "n_estimators": [120, 200, 300, 500, 800, 1200],
    "max_depth": [5, 8, 15, 25, 30]
}
# 交叉验证网格验证
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)
estimator.fit(x_train, y_train)

# 预测值
score = estimator.score(x_test, y_test)
print(score)

# 看最好的模型设置
a = estimator.best_estimator_
print(a)