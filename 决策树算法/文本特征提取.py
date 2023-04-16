#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def english_count_demo():
    data = ["life is short,i like python", "life is too long,i dislike python"]

    # 实例化stop_words停用词
    transfer = CountVectorizer(stop_words=[])

    # 进行特征化
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names_out())
    print(transfer_data.toarray())
    print(transfer_data)


def chinese_count_demo():
    # 这里一般需要切词器
    # pip install jieba
    data = ["人生 苦度，我用 python", "人生炫酷，我用JavaScript"]

    # 实例化stop_words停用词
    transfer = CountVectorizer(stop_words=[])

    # 进行特征化
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names_out())
    print(transfer_data.toarray())
    print(transfer_data)


def tfidf_count_demo():
    # 这里一般需要切词器
    # pip install jieba
    data = ["人生 苦度，我用 python", "人生炫酷，我用JavaScript"]

    # 分类机器学习，前期数据处理的方式之一
    transfer = TfidfVectorizer(stop_words=[])

    # 进行特征化
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names_out())
    print(transfer_data.toarray())
    print(transfer_data)


if __name__ == '__main__':
    # english_count_demo()
    # chinese_count_demo()
    tfidf_count_demo()
