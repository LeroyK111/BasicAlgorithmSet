#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入数据提取库
from sklearn.feature_extraction import DictVectorizer


def dict_demo():
    data = [
        {
            'city': '北京',
            'temperature': 100
        },
        {
            'city': '上海',
            'temperature': 60
        },
        {
            'city': '深圳',
            'temperature': 30
        },
    ]

    # 实例化字典特征提取器(为了便于理解，我们关闭sparse稀松格式化输出)
    transfer = DictVectorizer(sparse=False)

    # 调用fit_transform
    trans_data = transfer.fit_transform(data)

    # 这个是新api
    print("特征名字是:\n", transfer.get_feature_names_out())
    print(trans_data)


if __name__ == '__main__':
    dict_demo()