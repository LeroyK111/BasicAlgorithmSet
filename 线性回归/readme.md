# 线性回归

## ![image-20220729174527974](readme.assets/image-20220729174527974.png)

## 定义

多元回归公式

![image-20220729175322782](readme.assets/image-20220729175322782.png)

线性回归模型：一种是线性关系，另一种是非线性关系。

![线性回归是人工智能机器学习里面最基础的算法-电子发烧友网](readme.assets/o4YBAF57FBiAKBz0AAGfCLna-JQ066.png)

非线性模型

![09.0 非线性回归- AI-EDU](readme.assets/sin_data.png)

## API

![image-20220729180626335](readme.assets/image-20220729180626335.png)

![image-20220729181757864](readme.assets/image-20220729181757864.png)

## 求导公式（用来优化模型）

![image-20220729182000913](readme.assets/image-20220729182000913.png)

矩阵向量求导

![image-20220729182606075](readme.assets/image-20220729182606075.png)

## 线性回归的优化

![image-20220729183036157](readme.assets/image-20220729183036157.png)

### 正规方程

![image-20220729183507686](readme.assets/image-20220729183507686.png)

 推导方式一：

![image-20220729185240877](readme.assets/image-20220729185240877.png)

推导方式二

google吧😄

### 梯度下降

![image-20220729185803884](readme.assets/image-20220729185803884.png)

![image-20220729185827013](readme.assets/image-20220729185827013.png)

#### 梯度的概念

![image-20220729190224889](readme.assets/image-20220729190224889.png)

#### 单变量函数梯度下降

![image-20220729190541894](readme.assets/image-20220729190541894.png)

#### 多变量梯度下降

![image-20220729191225442](readme.assets/image-20220729191225442.png)

#### 梯度下降公式

![image-20220729191259480](readme.assets/image-20220729191259480.png)

α不要设置学习率太大or步长，导致无法找到最低点。

取负数，是为了确保是是为了找到最小值。

![image-20220729192005060](readme.assets/image-20220729192005060.png)

##### 梯度下降其他方法

全梯度下降算法（FG）

![image-20220729192434048](readme.assets/image-20220729192434048.png)

##### 随机梯度下降算法（SG）

![image-20220729192852873](readme.assets/image-20220729192852873.png)

##### 小批量梯度下降算法（mini-bantch）

![image-20220729192926911](readme.assets/image-20220729192926911.png)

##### 随机平均梯度下降算法（SAG）

![image-20220729193003236](readme.assets/image-20220729193003236.png)

算法比较

![image-20220729193800747](readme.assets/image-20220729193800747.png)

#### 梯度下降优化算法

![image-20220729193837517](readme.assets/image-20220729193837517.png)

### API高级

![image-20220729193946745](readme.assets/image-20220729193946745.png)

#### 回归性能评估

由于回归中的数据大小不一致，需要标准换处理。

![image-20220729195350259](readme.assets/image-20220729195350259.png)

## 欠拟合和过拟合

![image-20220730014721974](readme.assets/image-20220730014721974.png)

解决方法

![image-20220730014801790](readme.assets/image-20220730014801790.png)

### 正则化

![image-20220730015047033](readme.assets/image-20220730015047033.png)

![image-20220730015113726](readme.assets/image-20220730015113726.png)

![image-20220730015200354](readme.assets/image-20220730015200354.png)

#### 正则化类别

![image-20220730015353095](readme.assets/image-20220730015353095.png)

L2正则化：ridge岭回归

L1正则化： lasso回归

#### 维灾难

![image-20220730015545747](readme.assets/image-20220730015545747.png)

![image-20220730015601714](readme.assets/image-20220730015601714.png)

##### 维数灾难和过拟合![image-20220730015704071](readme.assets/image-20220730015704071.png)

![image-20220730015736411](readme.assets/image-20220730015736411.png)

![image-20220730015800480](readme.assets/image-20220730015800480.png)

二律背反： 维度数量和分类器，有一个平衡点

![image-20220730015931764](readme.assets/image-20220730015931764.png)

100维和10维之间的数据比较合适。

#### 正则化线性模型

##### ridge regression岭回归

![image-20220730020539946](readme.assets/image-20220730020539946.png)

##### lasso回归

![image-20220730020841737](readme.assets/image-20220730020841737.png)

![image-20220730020947659](readme.assets/image-20220730020947659.png)

##### Elastic Net弹性回归

![image-20220730021235214](readme.assets/image-20220730021235214.png)

 Early Stopping

![image-20220730021700174](readme.assets/image-20220730021700174.png)

#### 对应的api

![image-20220730022240418](readme.assets/image-20220730022240418.png)

正则化力度越大，权重系数就会越小。

## 模型保存和加载

存储格式：filename.joblib

![image-20220730024936253](readme.assets/image-20220730024936253.png)
