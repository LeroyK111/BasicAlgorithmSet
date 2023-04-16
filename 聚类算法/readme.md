# 聚类算法

## K-means算法原理

聚类，适合无监督学习。

![image-20220803213453497](readme.assets/image-20220803213453497.png)

### 使用场景

![image-20220803214326590](readme.assets/image-20220803214326590.png)

![image-20220803214353929](readme.assets/image-20220803214353929.png)

决策树，集成学习，回归，近邻都是监督学习算法。

### 具体使用方法

![image-20220803215015941](readme.assets/image-20220803215015941.png)

### 流程分析

![image-20220803215546737](readme.assets/image-20220803215546737.png)

### 聚类算法原理

![image-20220803224155641](readme.assets/image-20220803224155641.png)

![image-20220803224454131](readme.assets/image-20220803224454131.png)

![image-20220803225659974](readme.assets/image-20220803225659974.png)

每次迭代结果不变时，可以认为算法收敛，聚类完毕。

![image-20220803230716009](readme.assets/image-20220803230716009.png)

## 模型评估

### 误差平方和

![image-20220803233307755](readme.assets/image-20220803233307755.png)

![image-20220803233326442](readme.assets/image-20220803233326442.png)

![image-20220803233516476](readme.assets/image-20220803233516476.png)

质心的初始值很重要。

### 肘方法

![image-20220803233658859](readme.assets/image-20220803233658859.png)

拐点，就是最佳K值

### 轮廓系数法

![image-20220803233927664](readme.assets/image-20220803233927664.png)

### CH系数

![image-20220803235518770](readme.assets/image-20220803235518770.png)

类别内部数据的协方差越小越好，类别之间的协方差越大越好。

![image-20220804000227680](readme.assets/image-20220804000227680.png)

总结：

![image-20220804000437064](readme.assets/image-20220804000437064.png)

## 算法优化

![image-20220804000617982](readme.assets/image-20220804000617982.png)

### canopy算法配合初始聚类

画同心圆

![image-20220804004953508](readme.assets/image-20220804004953508.png)

![image-20220804004932376](readme.assets/image-20220804004932376.png)

还是欧式距离做半径，对范围内的样本进行检索。

### K-means++

![image-20220804005110477](readme.assets/image-20220804005110477.png)

![image-20220804005330627](readme.assets/image-20220804005330627.png)

### 二分K-means

![image-20220804005346149](readme.assets/image-20220804005346149.png)

![image-20220804005441576](readme.assets/image-20220804005441576.png)

## k-medoids（k中心聚集算法）

![image-20220804010149176](readme.assets/image-20220804010149176.png)

让代码更健壮

![image-20220804010207582](readme.assets/image-20220804010207582.png)

## kernel k-means算法

![image-20220804010430609](readme.assets/image-20220804010430609.png)

## ISODATA算法

![image-20220804010517651](readme.assets/image-20220804010517651.png)

## mini batch k-means(大数据算法)

![image-20220804010553031](readme.assets/image-20220804010553031.png)

## 总结

![image-20220804010619761](readme.assets/image-20220804010619761.png)

## 特征工程+特征降维

![image-20220804010647456](readme.assets/image-20220804010647456.png)

![image-20220804010817422](readme.assets/image-20220804010817422.png)

### 降维的方式

#### 特征选择

![image-20220804010858570](readme.assets/image-20220804010858570.png)

![image-20220804010917759](readme.assets/image-20220804010917759-16595465582341.png)

##### 低方差过滤方式

![image-20220804010933567](readme.assets/image-20220804010933567.png)

Api

![image-20220804011128963](readme.assets/image-20220804011128963.png)

只对特征值进行降维

![image-20220804011319184](readme.assets/image-20220804011319184.png)

![image-20220804015838298](readme.assets/image-20220804015838298.png)

如果需要更多方式去降维：

我们需要相关系数法

![image-20220804020122918](readme.assets/image-20220804020122918.png)

![image-20220804020156298](readme.assets/image-20220804020156298.png)

![image-20220804020213076](readme.assets/image-20220804020213076.png)

![image-20220804020654887](readme.assets/image-20220804020654887.png)

![image-20220804020717928](readme.assets/image-20220804020717928.png)

#### 主成分分析

##### PCA分析

![image-20220804021005105](readme.assets/image-20220804021005105.png)

##### API

![image-20220804021040912](readme.assets/image-20220804021040912.png)

### 案例

![image-20220804022135760](readme.assets/image-20220804022135760.png)

![image-20220804022151986](readme.assets/image-20220804022151986.png)

![image-20220804022454467](readme.assets/image-20220804022454467.png)





