# 逻辑回归算法

## 逻辑回归原理

![image-20220730025723338](readme.assets/image-20220730025723338.png)

将线性回归的结果再次进行判断

![image-20220730025801123](readme.assets/image-20220730025801123.png)

![image-20220730030113503](readme.assets/image-20220730030113503.png)

![image-20220730030131335](readme.assets/image-20220730030131335.png)

这个有点经验法的感觉了

## 损失以及优化

![image-20220730030337913](readme.assets/image-20220730030337913.png)

![image-20220730030425295](readme.assets/image-20220730030425295.png)

![image-20220730030501865](readme.assets/image-20220730030501865.png)

### 优化

![image-20220730031252942](readme.assets/image-20220730031252942.png)

## 逻辑回归API

![image-20220730031317824](readme.assets/image-20220730031317824.png)

## 分类评估方法

### 混淆矩阵（更像是笛卡尔积）

![image-20220802000706114](readme.assets/image-20220802000706114.png)

### 准确率和召回率

看查的准不准。。。

![](readme.assets/image-20220802000959289.png)

看查的全不全

![image-20220802001107180](readme.assets/image-20220802001107180.png)

### F1-score

反应模型的稳健性。

![image-20220802001512707](readme.assets/image-20220802001512707.png)

F1越接近1，效果越好

### 分类评估报告

![image-20220802001756619](readme.assets/image-20220802001756619.png)

## 如果样本不均衡(不满足随机分布)，我们该怎么处理?

使用ROC曲线和AUC指标

![image-20220802004124509](readme.assets/image-20220802004124509.png)

### ROC曲线

![image-20220802004546903](readme.assets/image-20220802004546903.png)

![image-20220802004932627](readme.assets/image-20220802004932627.png)

### AUC计算指标API

![image-20220802005150335](readme.assets/image-20220802005150335.png)

![image-20220802005208226](readme.assets/image-20220802005208226.png)

### 总结：

```
AUC只能用来评价二分类
AUC非常适合评价样本不平衡的分类器性能
```

![image-20220802011506109](readme.assets/image-20220802011506109.png)

查看第一种可能

![image-20220802010835372](readme.assets/image-20220802010835372.png)

第二种可能

![image-20220802011734485](readme.assets/image-20220802011734485.png)

第三种可能

![image-20220802011808050](readme.assets/image-20220802011808050.png)

说白了，就是通过图像面积，进一步了解ROC是什么。。

![image-20220802011435014](readme.assets/image-20220802011435014.png)













































