# 集成学习算法

混合算法。

![image-20220803005633644](readme.assets/image-20220803005633644.png)

![image-20220803005904617](readme.assets/image-20220803005904617.png)

集成学习中的boosting和Bagging

能够提升1%~2%

![image-20220803010144490](readme.assets/image-20220803010144490.png)

![image-20220803010157596](readme.assets/image-20220803010157596.png)

## Bagging集成原理

1.采样不同的数据

![image-20220803010601196](readme.assets/image-20220803010601196.png)

2.训练分类器

![image-20220803010613921](readme.assets/image-20220803010613921.png)

3.平权投票

![image-20220803010634127](readme.assets/image-20220803010634127.png)

同一份训练集，经过多次训练，得到不同的模型。每个模型输出都是

![image-20220803010955735](readme.assets/image-20220803010955735.png)

## 随机森林构造

也是为了解决**过拟合问题**。

![image-20220803012908474](readme.assets/image-20220803012908474.png)

![image-20220803013210898](readme.assets/image-20220803013210898.png)

就是训练多个决策树，然后对同一份测试集进行判断，多者为真。

### 随机森林API

超参数：无初始值的形参

![image-20220803013237031](readme.assets/image-20220803013237031.png)

优缺点：

bagging网格，一份数据使用通过一种算法，生成多个模型。然后对这些模型取平均值，提高模型泛化率

![image-20220803014711287](readme.assets/image-20220803014711287.png)

## boosting集成原理

这个就是可以动态添加分类器的模型算法，每加入一个弱学习器，整体能力就可以得到提升。**解决欠拟合。**

![image-20220803200515118](readme.assets/image-20220803200515118.png)

###  实现过程:

![image-20220803200733308](readme.assets/image-20220803200733308.png)

![image-20220803200804024](readme.assets/image-20220803200804024.png)

![image-20220803201212926](readme.assets/image-20220803201212926.png)

![image-20220803201233877](readme.assets/image-20220803201233877.png)

![image-20220803201251544](readme.assets/image-20220803201251544.png)

### 原理：让训练注意到错误数据上

![image-20220803201350640](readme.assets/image-20220803201350640.png)

![image-20220803201425044](readme.assets/image-20220803201425044.png)

### Api使用

![image-20220803204641611](readme.assets/image-20220803204641611.png)

## 两种集成的区别

![image-20220803204531792](readme.assets/image-20220803204531792.png)

## GBDT算法

这个就是又加入了一个梯度算法，梯度提升决策树

![image-20220803204734030](readme.assets/image-20220803204734030.png)

![image-20220803205003864](readme.assets/image-20220803205003864.png)

![image-20220803210421931](readme.assets/image-20220803210421931.png)

## XGBoost算法

![image-20220803210636196](readme.assets/image-20220803210636196.png)

### 泰勒展开式

最小二乘法（拟合）：  预测值和真实值之差的平方和。

![image-20220803210817389](readme.assets/image-20220803210817389.png)

