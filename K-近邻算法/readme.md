# K-近邻算法(KNN)概念

## 定义：

K Nearest Neighbor算法又叫KNN算法，这个算法是机器学习里面的一个比较经典的算法。

如果一个样本在特征空间中的**K个最相似(特征空间中最邻近)**的样本中的大多数属于某一个类别，则该样本也属于这个类别。

### **距离公式**

![image-20220728162709197](readme.assets/image-20220728162709197.png)

样本数据![image-20220728163554486](readme.assets/image-20220728163554486.png)

分别计算每个电影和被预测的电影距离，然后求解

![image-20220728164139288](readme.assets/image-20220728164139288.png)

机器学习库：

```
# 使用别人封装好的库
pip install -U scikit-learn
```

![image-20220728173826265](readme.assets/image-20220728173826265.png)

### 距离度量:

#### 欧式距离(坐标轴距离)

![image-20220728174529826](readme.assets/image-20220728174529826.png)

#### 曼哈顿距离

![image-20220728174838737](readme.assets/image-20220728174838737.png)

![image-20220728174937998](readme.assets/image-20220728174937998.png)

#### 切比雪夫距离(国际象棋)

只需要走目标值坐标的最大值即可。

![image-20220728175412549](readme.assets/image-20220728175412549.png)

![image-20220728175521294](readme.assets/image-20220728175521294.png)

#### 闵可夫斯基距离

![image-20220728175631638](readme.assets/image-20220728175631638.png)

 量纲不同。![image-20220728180049512](readme.assets/image-20220728180049512.png)

#### 标准化欧式距离

![image-20220728180229294](readme.assets/image-20220728180229294.png)

#### 余弦距离

向量算法

![image-20220728180522717](readme.assets/image-20220728180522717.png)

#### 汉明距离

主要用来解决

#### ![image-20220728180638253](readme.assets/image-20220728180638253.png)

![image-20220728180854316](readme.assets/image-20220728180854316.png)

#### 杰卡德距离

![image-20220728181345985](readme.assets/image-20220728181345985.png)

#### 马氏距离

![image-20220728181823662](readme.assets/image-20220728181823662.png)

![image-20220728181857967](readme.assets/image-20220728181857967.png)

案例

![image-20220728182327080](readme.assets/image-20220728182327080.png)

![image-20220728182343475](readme.assets/image-20220728182343475.png)

### K值的选择

![image-20220728182506194](readme.assets/image-20220728182506194.png)

K值选择问题

![image-20220728182605349](readme.assets/image-20220728182605349.png)

### KD树构造

![image-20220728183202220](readme.assets/image-20220728183202220.png)

二叉树

![image-20220728183357153](readme.assets/image-20220728183357153.png)

![image-20220728183608033](readme.assets/image-20220728183608033.png)

![image-20220728183624592](readme.assets/image-20220728183624592.png)

树的构造方法

![image-20220728183650206](readme.assets/image-20220728183650206.png)

#### 树的建立

从方差大的维度进行切割，说明离散程度高

![image-20220728183803440](readme.assets/image-20220728183803440.png)

![image-20220728183917490](readme.assets/image-20220728183917490.png)

思路整理

![image-20220728185355467](readme.assets/image-20220728185355467.png)

最近领域的搜索

![image-20220728185534319](readme.assets/image-20220728185534319.png)

![image-20220728185634607](readme.assets/image-20220728185634607.png)

```
1.节点判断
先从一个维度靠近，然后求一次距离r，用r做半径在画圈。
2.回溯
回溯的目的是为了避免有其他节点遗漏，当在半径为R的范围内时，需要不断更新r 的距离，直到有一个最小值r的出现，则可以判断该节点与测试点最相近。
3.结束搜索
通过各个节点到测点的r进行比较，给出测试点的预测特征。
```

