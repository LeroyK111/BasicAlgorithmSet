#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
预估波士顿房价
"""

# 请求数据
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, RidgeCV
# 模型评估
from sklearn.metrics import mean_absolute_error


def linear_model1():
    # 获取数据
    boston = load_boston()
    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(
        boston.data, boston.target, test_size=.2, random_state=22)

    # 特征工程,标准化
    transfer = StandardScaler()
    # 将训练集和测试集,都标准化
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 使用岭回归算法
    # estimator = Ridge()
    # 加入正则化alphas力度
    estimator = RidgeCV(alphas=(.001, .1, 1, 10, 100))
    estimator.fit(x_train, y_train)

    # 模型评估
    y_pre = estimator.predict(x_test)
    print("预测值是:", y_pre)
    score = estimator.score(x_test, y_test)
    print("准确率:", score)

    # 局方误差评判
    ret = mean_absolute_error(y_test, y_pre)
    print("均方误差是", ret)


if __name__ == '__main__':
    linear_model1()
