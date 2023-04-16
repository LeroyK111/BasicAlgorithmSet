# 决策树算法简介

![image-20220802102856140](readme.assets/image-20220802102856140.png)

概念来源于信息论中的知识：信息熵，信息增益

信息熵值：描述系统混乱程度的值。

![image-20220802103355113](readme.assets/image-20220802103355113.png)

信息增益：以某特征划分数据集前后的熵的差值。

![image-20220802103828449](readme.assets/image-20220802103828449.png)

![image-20220802104805898](readme.assets/image-20220802104805898.png)

![image-20220802111228412](readme.assets/image-20220802111228412.png)

这里需要《机器学习》书本解释

![image-20220802111538908](readme.assets/image-20220802111538908.png)

## 总结:

![image-20220802115517478](readme.assets/image-20220802115517478.png)

![image-20220802115529132](readme.assets/image-20220802115529132.png)

## 常见决策树

![image-20220802115733896](readme.assets/image-20220802115733896.png)

![image-20220802115757876](readme.assets/image-20220802115757876.png)

### ID3算法

![image-20220802115821948](readme.assets/image-20220802115821948.png)

信息增益 = entroy（前）-entroy（后）

信息增益越大，则我们有限选择这个属性进行计算，信息增益优先选择属性总类别多的进行划分。

### C4.5算法

![image-20220802115859705](readme.assets/image-20220802115859705.png)

### CART算法

![image-20220802120005707](readme.assets/image-20220802120005707.png)

## cart剪支

![image-20220802120711105](readme.assets/image-20220802120711105.png)

 ![image-20220802120734123](readme.assets/image-20220802120734123.png)

预剪枝：

![image-20220802120854995](readme.assets/image-20220802120854995.png)

后剪枝:

![image-20220802121138098](readme.assets/image-20220802121138098.png)

## 特征提取

#### 字典特征提取

![image-20220802121439761](readme.assets/image-20220802121439761.png)

总结：对于特征中存在类别信息的我们都会做one-hot编码

#### 文本特征提取

![image-20220802123100345](readme.assets/image-20220802123100345.png)

#### Tf-idf文本特征提取

![image-20220802160142797](readme.assets/image-20220802160142797.png)

 这是一个分数特征，tfi-idf越大，这个词语的重要性越高。

![image-20220802220000417](readme.assets/image-20220802220000417.png)

#### 图像特征提取

这里就涉及到deep learnin，主要是RGB像素点了，天生就是三维数据。

## 决策树算法api

![image-20220802220135711](readme.assets/image-20220802220135711.png)

保存树结构dot文件

![image-20220802235526569](readme.assets/image-20220802235526569.png)

![1](readme.assets/1.png)

## 总结

![image-20220803001407897](readme.assets/image-20220803001407897.png)

剪枝cart算法（解决过拟合），可以直接在api里设置。

![image-20220803004058748](readme.assets/image-20220803004058748.png)
