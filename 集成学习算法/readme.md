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

![image-20220803012908474](readme.assets/image-20220803012908474.png)

![image-20220803013210898](readme.assets/image-20220803013210898.png)

就是训练多个决策树，然后对同一份测试集进行判断，多者为真。

### 随机森岭API

超参数：无初始值的形参

![image-20220803013237031](readme.assets/image-20220803013237031.png)

优缺点：

![image-20220803014711287](readme.assets/image-20220803014711287.png)