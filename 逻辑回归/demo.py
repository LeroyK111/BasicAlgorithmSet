#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

# 分类评估参数
from sklearn.metrics import classification_report

# 直接给与列名
names = [
    "Sample code number", "Clump Thickness", "Uniformity of Cell Size",
    "Uniformity of Cell Shape", "Marginal Adhesion",
    "Single Epithelial Cell Size", "Bare Nuclei", "Normal Nucleoli", "Mitoses",
    "Class"
]
# 导入乳腺癌数据
data = pd.read_csv(
    names=names,
    filepath_or_buffer="learning/机器学习/自学算法/逻辑回归/breast-cancer-wisconsin.data")

# 清洗数据
# 缺失值处理
data = data.replace(to_replace="?", value=np.nan)
# 直接删除那一行样本
data = data.dropna()

# 确定特征值和目标值
x = data.iloc[:, 1:10]
y = data["Class"]

# 分割数据
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=.2, random_state=22)

# 特征工程（标准化）
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 机器学习（逻辑回归，说白了，就是判断对和错）
estimator = LogisticRegression()
# 就是导入x和y的训练集
estimator.fit(x_train, y_train)

# 模型基本评估
y_predict = estimator.predict(x_test)
print(y_predict)
# 比较准确率
score = estimator.score(x_test, y_test)
print(score)

# 使用分类评估
ret = classification_report(
    y_test, y_predict, labels=(2, 4), target_names=("良性", "恶性"))
print(ret)

# 不平衡二分类的解决方法
from sklearn.metrics import roc_auc_score

y_test = np.where(y_test > 3, 1, 0)
done = roc_auc_score(y_true=y_test, y_score=y_predict)
print(done)
