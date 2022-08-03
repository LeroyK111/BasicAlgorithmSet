#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# 导入相关系数
from scipy.stats import pearsonr, spearmanr


def var_thr():
    x1 = [123, 123, 214, 234, 253]
    x2 = [12, 123, 234, 534, 1124]
    ret = pearsonr(x1, x2)
    print("这两列数据皮尔逊相关系数为", ret)
    ret2 = spearmanr(x1, x2)
    print("这两列数据斯皮尔慢相关系数为", ret2)


if __name__ == '__main__':
    var_thr()