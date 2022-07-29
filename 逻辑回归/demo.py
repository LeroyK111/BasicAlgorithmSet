#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

import ssl

# 禁止证书校验
ssl._create_default_https_context = ssl._create_unverified_context

names = []
# 导入乳腺癌数据
data = pd.read_csv(
    filepath_or_buffer="learning/机器学习/自学算法/逻辑回归/breast-cancer-wisconsin.data",
    names=names)
print(data)
