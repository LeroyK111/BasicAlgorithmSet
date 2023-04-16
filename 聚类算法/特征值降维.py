#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold


def var_thr():
    """
    特征选择，低方差特征过滤
    """
    data = pd.DataFrame(np.random.randint(1, 100, (2000, 12)))
    """
         Unnamed: 0    Mkt-RF       SMB       HML        RF
    """
    # 实例化一个选择器,threshold=阈值必须填写，会尽量降维到threshold
    transfer = VarianceThreshold(threshold=7)
    transfer_data = transfer.fit_transform(data.iloc[:, 1:12])
    # 减少了一个特征值
    print(transfer_data.shape)


if __name__ == '__main__':
    var_thr()