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













