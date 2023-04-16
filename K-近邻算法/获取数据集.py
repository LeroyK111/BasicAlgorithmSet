#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入已有数据集
from sklearn.datasets import load_iris, fetch_20newsgroups
import pandas as pd
import seaborn as sns
# 使用数据集划分
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# 中文字符导入,解决乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 大数据集获取,这个网络请求
# news = fetch_20newsgroups()
# print(news)

# 这个是内置数据集
iris = load_iris()
# print("特征值:\n", iris.data)
# print("目标值:\n", iris.target)
# print("特征值名字:\n", iris.feature_names)
# print("目标值名字:\n", iris.target_names)
# print("数据集描述:\n", iris.DESCR)

iris_d = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
# 插入一列目标值
iris_d["target"] = iris.target
# print(iris_d)


def plot_iris(data, col1, col2):
    sns.lmplot(x=col1, y=col2, data=data, hue="target", fit_reg=False)
    plt.title("鸢尾花数据展示")
    plt.xlabel(col1)
    plt.xlabel(col2)
    plt.pause(8)


# plot_iris(iris_d, "sepal_length", "petal_width")

# 数据集划分（test_size测试集划分比例，random_state随机种子）
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=.2, random_state=22)

# 看看测试集和训练集的区别
# print(y_train.shape)
# print(y_test.shape)
