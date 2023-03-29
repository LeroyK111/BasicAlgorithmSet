# 常见python解法

## 数据结构

### 为什么要学习数据结构和算法？

随着应用程序变得越来越复杂和数据越来越丰富，几百万、几十亿甚至几百亿的数据就会出现，而对这么大对数据进行搜索、插入或者排序等的操作就越来越慢，数据结构就是用来解决这些问题的。

![](数据结构.png)

常用数据结构一共有九种。

### 数据与内存
计算机中的数据，我们能够想到文本、图片、视频、语音、3D 模型等等，这些数据虽然组织形式不同，但都是由各种基本数据类型构成的。

**「基本数据类型」是 CPU 可以直接进行运算的类型，在算法中直接被使用**。

-   「整数」根据不同的长度分为 byte, short, int, long ，根据算法需求选用，即在满足取值范围的情况下尽量减小内存空间占用；
-   「浮点数」代表小数，根据长度分为 float, double ，同样根据算法的实际需求选用；
-   「字符」在计算机中是以字符集的形式保存的，char 的值实际上是数字，代表字符集中的编号，计算机通过字符集查表来完成编号到字符的转换。占用空间通常为 2 bytes 或 1 byte ；
-   「布尔」代表逻辑中的“是”与“否”，其占用空间需根据编程语言确定，通常为 1 byte 或 1 bit ；
![](Pasted%20image%2020230325204258.png)

### 计算机内存

![](Pasted%20image%2020230325204511.png)


### 应用实例

**本部分由python实现，JavaScript逻辑一样。**

至于进一步加快计算过程，还需要多线程多进场协程等配合，常用的还是集群计算框架。

### Algorithm算法

**专门用来解决某个问题而写的专用计算方法。**

算法（Algorithm）是指用来操作数据、解决程序问题的一组方法。对于同一个问题，使用不同的算法，也许最终得到的结果是一样的，但在过程中消耗的资源和时间却会有很大的区别。  
那么我们应该如何去衡量不同算法之间的优劣呢？
主要还是从算法所占用的「时间」和「空间」两个维度去考量。

-   时间维度：是指执行当前算法所消耗的时间，我们通常用「时间复杂度」来描述。
-   空间维度：是指执行当前算法需要占用多少内存空间，我们通常用「空间复杂度」来描述。

因此，评价一个算法的效率主要是看它的时间复杂度和空间复杂度情况。然而，有的时候时间和空间却又是「鱼和熊掌」，不可兼得的，那么我们就需要从中去取一个平衡点。

下面分别介绍一下「时间复杂度」和「空间复杂度」的计算方式。

#### 时间复杂度

想要知道一个算法的「时间复杂度」，很多人首先想到的的方法就是把这个算法程序运行一遍，那么它所消耗的时间就自然而然知道了。

这种方式可以吗？当然可以，不过它也有很多弊端。  
这种方式非常容易受运行环境的影响，在性能高的机器上跑出来的结果与在性能低的机器上跑的结果相差会很大。而且对测试时使用的数据规模也有很大关系。再者，并我们在写算法的时候，还没有办法完整的去运行呢。

因此，另一种更为通用的方法就出来了：

「 **大O符号表示法** 」，即 T(n) = O(f(n))

```js
for(i=1; i<=n; ++i)
{
   j = i;
   j++;
}
```
通过「 大O符号表示法 」，这段代码的时间复杂度为：O(n) ，为什么呢?

在 大O符号表示法中，时间复杂度的公式是： T(n) = O( f(n) )，其中f(n) 表示每行代码执行次数之和，而 O 表示正比例关系，这个公式的全称是：**算法的渐进时间复杂度**。

颗粒度，就是开始➡完成之间的 环节数量。

<div style="color: red;">
继续看上面的例子，假设每行代码的执行时间都是一样的，我们用 1颗粒时间 来表示，那么这个例子的第一行耗时是1个颗粒时间，第三行的执行时间是 n个颗粒时间，第四行的执行时间也是 n个颗粒时间（第二行和第五行是符号，暂时忽略），那么总时间就是 1颗粒时间 + n颗粒时间 + n颗粒时间 ，即 (1+2n)个颗粒时间，即： T(n) = (1+2n)*颗粒时间，从这个结果可以看出，这个算法的耗时是随着n的变化而变化，因此，我们可以简化的将这个算法的时间复杂度表示为：T(n) = O(n)
</div>

为什么可以这么去简化呢，因为大O符号表示法并不是用于来真实代表算法的执行时间的，它是用来表示代码执行时间的增长变化趋势的。

所以上面的例子中，如果n无限大的时候，T(n) = time(1+2n)中的常量1就没有意义了，倍数2也意义不大。因此直接简化为T(n) = O(n) 就可以了。


##### 常见的时间复杂度量级有：
-   常数阶O(1)
-   对数阶O(logN)
-   线性阶O(n)
-   线性对数阶O(nlogN)
-   平方阶O(n²)
-   立方阶O(n³)
-   K次方阶O(n^k)
-   指数阶(2^n)
上面从上至下依次的时间复杂度越来越大，执行的效率越来越低。

所谓算法优化，就是按照量级将计算过程往简化走。

1.  **常数阶O(1)**
无论代码执行了多少行，只要是没有循环等复杂结构，那这个代码的时间复杂度就都是O(1)，如：
```js
int i = 1;
int j = 2;
++i;
j++;
int m = i + j;
```
上述代码在执行的时候，它消耗的时候并不随着某个变量的增长而增长，那么无论这类代码有多长，即使有几万几十万行，都可以用O(1)来表示它的时间复杂度。

2.  **对数阶O(logN)**

还是先来看代码：

```js
int i = 1;
while(i<n)
{
    i = i * 2;
}
```

从上面代码可以看到，在while循环里面，每次都将 i 乘以 2，乘完之后，i 距离 n 就越来越近了。我们试着求解一下，假设循环x次之后，i 就大于 2 了，此时这个循环就退出了，也就是说 2 的 x 次方等于 n，那么 x = log2^n  
也就是说当循环 log2^n 次以后，这个代码就结束了。因此这个代码的时间复杂度为：**O(logn)**

3.  **线性阶O(n)**

这个在最开始的代码示例中就讲解过了，如：

```js
for(i=1; i<=n; ++i)
{
   j = i;
   j++;
}
```

这段代码，for循环里面的代码会执行n遍，因此它消耗的时间是随着n的变化而变化的，因此这类代码都可以用O(n)来表示它的时间复杂度。

4.  **线性对数阶O(nlogN)**

线性对数阶O(nlogN) 其实非常容易理解，将时间复杂度为O(logn)的代码循环N遍的话，那么它的时间复杂度就是 n * O(logN)，也就是了O(nlogN)。

就拿上面的代码加一点修改来举例：

```js
for(m=1; m<n; m++)
{
    i = 1;
    while(i<n)
    {
        i = i * 2;
    }
}
```

5.  **平方阶O(n²)**

平方阶O(n²) 就更容易理解了，如果把 O(n) 的代码再嵌套循环一遍，它的时间复杂度就是 O(n²) 了。  
举例：

```js
for(x=1; i<=n; x++)
{
   for(i=1; i<=n; i++)
    {
       j = i;
       j++;
    }
}
```

这段代码其实就是嵌套了2层n循环，它的时间复杂度就是 O(n*n)，即 O(n²)  
如果将其中一层循环的n改成m，即：

```js
for(x=1; i<=m; x++)
{
   for(i=1; i<=n; i++)
    {
       j = i;
       j++;
    }
}
```

那它的时间复杂度就变成了 O(m*n)

5.  **立方阶O(n³)**、**K次方阶O(n^k)**

参考上面的O(n²) 去理解就好了，O(n³)相当于三层n循环，其它的类似。
就是循环嵌套。

```js
for(x=1; i<=m; x++)
{
   for(i=1; i<=n; i++)
    {
	   for(i=1; i<=n; i++)
	    {
	       j = i;
	       j++;
	    }
    }
}
```

6.  指数阶(2^n)
不可接受的算法，必须要优化。
```js
/* 指数阶（循环实现） */
function exponential(n) {
    let count = 0, base = 1;
    // cell 每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < base; j++) {
            count++;
        }
        base *= 2;
    }
    // count = 1 + 2 + 4 + 8 + .. + 2^(n-1) = 2^n - 1
    return count;
}
```
除此之外，其实还有 平均时间复杂度、均摊时间复杂度、最坏时间复杂度、最好时间复杂度 的分析方法，有点复杂，这里就不展开了。
https://www.hello-algo.com/chapter_computational_complexity/time_complexity/#226


```js
/* 生成一个数组，元素为 { 1, 2, ..., n }，顺序被打乱 */
function randomNumbers(n) {
    const nums = Array(n);
    // 生成数组 nums = { 1, 2, 3, ..., n }
    for (let i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    // 随机打乱数组元素
    for (let i = 0; i < n; i++) {
        const r = Math.floor(Math.random() * (i + 1));
        const temp = nums[i];
        nums[i] = nums[r];
        nums[r] = temp;
    }
    return nums;
}

/* 查找数组 nums 中数字 1 所在索引 */
function findOne(nums) {
    for (let i = 0; i < nums.length; i++) {
        // 当元素 1 在数组头部时，达到最佳时间复杂度 O(1)
        // 当元素 1 在数组尾部时，达到最差时间复杂度 O(n)
        if (nums[i] === 1) {
            return i;
        }
    }
    return -1;
}

```

#### 空间复杂度

「空间复杂度 Space Complexity」统计 **算法使用内存空间随着数据量变大时的增长趋势**。这个概念与时间复杂度很类似。
![](Pasted%20image%2020230325201740.png)

算法运行中，使用的内存空间主要有以下几种：
-   「输入空间」用于存储算法的输入数据
-   「暂存空间」用于存储算法运行中的变量、对象、函数上下文等数据
-   「输出空间」用于存储算法的输出数据
通常情况下，空间复杂度统计范围是「暂存空间」+「输出空间」。

```js
/* 类 */
class Node {
    val;
    next;
    constructor(val) {
        this.val = val === undefined ? 0 : val; // 结点值
        this.next = null;                       // 指向下一结点的引用
    }
}

/* 函数 */
function constFunc() {
    // do something
    return 0;
}

function algorithm(n) {       // 输入数据
    const a = 0;              // 暂存数据（常量）
    let b = 0;                // 暂存数据（变量）
    const node = new Node(0); // 暂存数据（对象）
    const c = constFunc();    // 栈帧空间（调用函数）
    return a + b + c;         // 输出数据
}
```

##### 推算方法

空间复杂度的推算方法和时间复杂度总体类似，只是从统计“计算操作数量”变为统计“使用空间大小”。与时间复杂度不同的是，**我们一般只关注「最差空间复杂度」**。这是因为内存空间是一个硬性要求，我们必须保证在所有输入数据下都有足够的内存空间预留。

**最差空间复杂度中的“最差”有两层含义**，分别为输入数据的最差分布、算法运行中的最差时间点。

-   **以最差输入数据为准**。当 n<10 时，空间复杂度为 n(1) ；但是当 n>10 时，初始化的数组 `nums` 使用 n(n) 空间；因此最差空间复杂度为 n(n) 

-   **以算法运行过程中的峰值内存为准**。程序在执行最后一行之前，使用 n(1) 空间；当初始化数组 `nums` 时，程序使用 n(n) 空间；因此最差空间复杂度为 n(n) ；

```js
function algorithm(n) {
    const a = 0;                   // O(1)
    const b = new Array(10000);    // O(1)
    if (n > 10) {
        const nums = new Array(n); // O(n)
    }
}
```
**在递归函数中，需要注意统计栈帧空间**。例如函数 `loop()`，在循环中调用了 n 次 `function()` ，每轮中的 `function()` 都返回并释放了栈帧空间，因此空间复杂度仍为 n(1) 。而递归函数 `recur()` 在运行中会同时存在 n 个未返回的 `recur()` ，从而使用 O(n) 的栈帧空间。
```js
function constFunc() {
    // do something
    return 0;
}
/* 循环 O(1) */
function loop(n) {
    for (let i = 0; i < n; i++) {
        constFunc();
    }
}
/* 递归 O(n) */
function recur(n) {
    if (n === 1) return;
    return recur(n - 1);
}
```

##### 空间复杂度量级:

![](Pasted%20image%2020230325202448.png)

1. 常数阶O(1)

常数阶常见于数量与输入数据大小 n 无关的**常量、变量、对象。**
需要注意的是，在循环中初始化变量或调用函数而占用的内存，在进入下一循环后就会被释放，即不会累积占用空间，空间复杂度仍为 O(1) 。

```js
/* 常数阶 */
function constant(n) {
    // 常量、变量、对象占用 O(1) 空间
    const a = 0;
    const b = 0;
    const nums = new Array(10000);
    const node = new ListNode(0);
    // 循环中的变量占用 O(1) 空间
    for (let i = 0; i < n; i++) {
        const c = 0;
    }
    // 循环中的函数占用 O(1) 空间
    for (let i = 0; i < n; i++) {
        constFunc();
    }
}
```


2. 线性阶O(n)
线性阶常见于元素数量与 n 成正比的数组、链表、栈、队列等。
```js
/* 线性阶 */
function linear(n) {
    // 长度为 n 的数组占用 O(n) 空间
    const nums = new Array(n);
    // 长度为 n 的列表占用 O(n) 空间
    const nodes = [];
    for (let i = 0; i < n; i++) {
        nodes.push(new ListNode(i));
    }
    // 长度为 n 的哈希表占用 O(n) 空间
    const map = new Map();
    for (let i = 0; i < n; i++) {
        map.set(i, i.toString());
    }
}

```

3. 平方阶O(n^2)
平方阶常见于元素数量与 n成平方关系的矩阵、图。
```js
/* 平方阶 */
function quadratic(n) {
    // 矩阵占用 O(n^2) 空间
    const numMatrix = Array(n).fill(null).map(() => Array(n).fill(null));
    // 二维列表占用 O(n^2) 空间
    const numList = [];
    for (let i = 0; i < n; i++) {
        const tmp = [];
        for (let j = 0; j < n; j++) {
            tmp.push(0);
        }
        numList.push(tmp);
    }
}
```


4. 指数阶O(2^n)
指数阶常见于二叉树。高度为 n 的「满二叉树」的结点数量为 2^n−1 ，使用 O(2^n) 空间。
```js
/* 指数阶（建立满二叉树） */
function buildTree(n) {
    if (n === 0) return null;
    const root = new TreeNode(0);
    root.left = buildTree(n - 1);
    root.right = buildTree(n - 1);
    return root;
}
```

5. 对数阶O(log n)
对数阶常见于分治算法、数据类型转换等。

例如「归并排序」，长度为 n 的数组可以形成高度为 log⁡ n 的递归树，因此空间复杂度为 O(log⁡ n) 。

再例如「数字转化为字符串」，输入任意正整数 n ，它的位数为 log10⁡ n ，即对应字符串长度为 log10⁡ n ，因此空间复杂度为 O(log10⁡ n)=O(log⁡ n) 。

```js
/* 合并左子数组和右子数组 */
// 左子数组区间 [left, mid]
// 右子数组区间 [mid + 1, right]
function merge(nums, left, mid, right) {
    // 初始化辅助数组
    let tmp = nums.slice(left, right + 1);   
    // 左子数组的起始索引和结束索引  
    let leftStart = left - left, leftEnd = mid - left;
    // 右子数组的起始索引和结束索引       
    let rightStart = mid + 1 - left, rightEnd = right - left;
    // i, j 分别指向左子数组、右子数组的首元素
    let i = leftStart, j = rightStart;                
    // 通过覆盖原数组 nums 来合并左子数组和右子数组
    for (let k = left; k <= right; k++) {
        // 若“左子数组已全部合并完”，则选取右子数组元素，并且 j++
        if (i > leftEnd) {
            nums[k] = tmp[j++];
        // 否则，若“右子数组已全部合并完”或“左子数组元素 <= 右子数组元素”，则选取左子数组元素，并且 i++
        } else if (j > rightEnd || tmp[i] <= tmp[j]) {
            nums[k] = tmp[i++];
        // 否则，若“左右子数组都未全部合并完”且“左子数组元素 > 右子数组元素”，则选取右子数组元素，并且 j++
        } else {
            nums[k] = tmp[j++];
        }
    }
}

/* 归并排序 */
function mergeSort(nums, left, right) {
    // 终止条件
    if (left >= right) return;       // 当子数组长度为 1 时终止递归
    // 划分阶段
    let mid = Math.floor((left + right) / 2);    // 计算中点
    mergeSort(nums, left, mid);      // 递归左子数组
    mergeSort(nums, mid + 1, right); // 递归右子数组
    // 合并阶段
    merge(nums, left, mid, right);
}

```


## 算法

数据结构研究的内容：就是如何按一定的逻辑结构，把数据组织起来，并选择适当的存储表示方法把逻辑结构组织好的数据存储到计算机的存储器里。算法研究的目的是为了更有效的处理数据，提高数据运算效率。数据的运算是定义在数据的逻辑结构上，但运算的具体实现要在存储结构上进行。一般有以下几种常用运算：

-   检索：检索就是在数据结构里查找满足一定条件的节点。一般是给定一个某字段的值，找具有该字段值的节点。
-   插入：往数据结构中增加新的节点。
-   删除：把指定的结点从数据结构中去掉。
-   更新：改变指定节点的一个或多个字段的值。
-   排序：把节点按某种指定的顺序重新排列。例如递增或递减。


## 数学公式的实现
斐波那契数列：这个数列从第3项开始，每一项都等于前两项之和。

质数列: 素数,除了1和它本身,其他数都不能整除。

## 常考的一些算法
冒泡排序：双循环，进行两两间对比，始终把大数后移.

选择排序（基于索引）： 双循环，选择最小（大）的一个数，记录其索引，每当运行到最外层循环时，进行位置替换。

插入排序：我们选择的值current不断的调整位置，这个索引上原先的值不断向后移动一个位置，因为current本身就是在后面取到的值，故而空出来一个索引位置，不会影响全列表的排序。

希尔排序（优化插入排序）：先将整个待排序的记录序列分割成为若干子序列（多个切片，然后插入排序，再拼接整体，再插入排序）分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。

归并排序：分而治之，将列表拆成两部分，互相比较其中的首元素以此来构造新的列表

快速排序：递归的分而治之，写起来麻烦,推荐伪代码

堆排序: 类似二叉树,让子节点键值小于它的父节点.

计数排序: 对元素进行加权,以确定每个元素的位置,生成新的列表.

桶排序: 对列表进行离散,然后分桶排序(任选一个排序算法),最后记得按照桶范围依次相加,生成新的列表.

基数排序: 根据键值的每位数字来分配桶,就是按照不同数量级的进行分桶,然后在同数量级的桶内进行排序,然后再生成新的列表.

深度优先搜索：stack栈，先入后出，后人先出

广度优先搜索：queue队列，先入先出，后入后出

二分搜索：有序列表中折中搜索

分治法：分桶

回溯算法：回溯算法说白了就是穷举法。

回溯算法的基本思想是：从一条路往前走，能进则进，不能进则退回来，换一条路再试。[八皇后问题](https://baike.baidu.com/item/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98?fromModule=lemma_inlink)就是回溯算法的典型，第一步按照顺序放一个皇后，然后第二步符合要求放第2个皇后，如果没有位置符合要求，那么就要改变第一个皇后的位置，重新放第2个皇后的位置，直到找到符合条件的位置就可以了。回溯在迷宫搜索中使用很常见，就是这条路走不通，然后返回前一个路口，继续下一条路。

贪心算法：局部最优解。

例如，平时购物找零钱时，为使找回的零钱的硬币数最少，不要求找零钱的所有方案，而是从最大面值的币种开始，按递减的顺序考虑各面额，先尽量用大面值的面额，当不足大面值时才去考虑下一个较小面值，这就是贪心算法

动态规划：需要找递推规律。

动态规划（Dynamic programming）是一种在数学、计算机科学和经济学中使用的，通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。 动态规划常常适用于有重叠子问题和最优子结构性质的问题，动态规划方法所耗时间往往远少于朴素解法。

##  leetcode解法
链表，图，二叉树等等概念，都是C/C++等面向过程语言提出来的指针概念，但是python or javasript 是面向对象的语言，对象对指针进行高级封装。莫要痴迷这个东西，只要能实现结果，剩下的就是优化算法，提高效率了。

1.两数之和 two_sum

2.添加两数 addTwoNum

3.最长不重复字符子串的长度 sonShort

4.重排数组，找中位数 TwoSortedArrays

5.相同字母包裹的最长子串 LongestPalindromicSubstring

6.字符串格式化，让字符串按指定行数展开 ZigzagConversion

7.反转数字 ReverseInteger

8.字符串转整数 StringtoInteger

9.倒序数字和正序数字一样大 PalindromeNumber

10.模拟正则表达式匹配 RegularExpressionMatching

11.装水最多的容器 ContainerWithMostWater

12.整数转罗马数字 IntegerToRoman

13.罗马数字转整数

14.最长公共前缀 LongestCommonPrefix

15.任取三个元素,相加等于0即可 3Sum

16.找出三个元素和给定值最接近的 3SumClosest

17.电话号码的字母组合 LetterCombinationsofaPhoneNumber

18.四个元素相加等于 4Sum

19.删除指定节点 RemoveNthNodeFromEndofList

20.有效括号 ValidParentheses

21.合并列表 MergeTwoSortedLists

22.给的括号数量，生成全部的括号种类 GenerateParentheses

23.合并K全部列表并排序 MergekSortedLists

24.交换一个列表相邻的一对元素 SwapNodesinPairs

25.指定反转节点数K ReverseNodesinkGroup

26.删除排序数组中的重复元素,用_代替 RemoveDuplicatesfromSortedArray

27.删除排序数组的指定元素，用_代替 RemoveElement

28.找到子串 FindtheIndexoftheFirstOccurrenceinaString

29.整数相除，商取整 DivideTwoIntegers

30.所有单词连接的子字符串 SubstringwithConcatenationofAllWords

31.下一种排列（这种排序没什么意义） NextPermutation

32.可能存在的括号 LongestValidParentheses

33.找列表中的元素 SearchinRotatedSortedArray

34.找到列表中首尾字符所在的位置 FindFirstandLastPositionofElementinSortedArray

35.推断应该在的位置 SearchInsertPosition

36.数独验证 ValidSudoku

37.填写数独(需要开多进程，不然太慢) SudokuSolver

38.数字拆分成加数的形式。CountandSay

39.用给出元素组合出目标值（重复使用）。CombinationSum

40.用给出元素组合出目标值（不重复使用）。 CombinationSumII

41.找到最小的缺失正整数。 FirstMissingPositive

42.计算凹槽最大的面积 TrappingRainWater

43.字符串转数字，再相乘 MultiplyStrings

44.通配符匹配 WildcardMatching

45.跳跃索引 JumpGameII

46.全排列 Permutations

47.全排列进阶 PermutationsII

48.旋转矩阵 RotateImage

49.字母相同字符串分在同一组 GroupAnagrams

50.指数 Pow

51.棋子占位问题 N-Queens

52.棋子占位问题2 N-QueensII

53.子数组最大和 MaximumSubarray

54.螺旋矩阵 spiral-matrix

55.跳跃游戏 jump-game

56.合并区间 MergeIntervals

57.插入区间再合并 InsertInterval

58.最后一个单词长度 lastWordLen

59.螺旋矩阵II spiral-matrix-ii

60.排列序列 permutation-sequence

61.旋转链表 rotate-list

62.不同路径 unique-paths

63.不同路径II unique-paths-ii

64.最小路径和 minimum-path-sum

65.有效数字 valid-number

66.加一 plus-one

67.二进制求和 add-binary

68.文本左右对齐 text-justification

69.x的平方根 sqrtx

70.爬楼梯 climbing-stairs

71.简化路径 simplify-path

72.编辑距离 edit-distance

73.矩阵置零 set-matrix-zeroes

74.高效索引 search-a-2d-matrix

75.颜色分类 sort-colors

76.最小覆盖子串 minimum-window-substring

77.组合 combinations

78.探索子集 subsets

79.单词搜索 wordSearch

80.删除有序数组中的重复项 II remove-duplicates-from-sorted-array-i

81.搜索旋转排序数组II search-in-rotated-sorted-array-ii

82.删除排序链表中的重复元素II remove-duplicates-from-sorted-list-ii

83.删除排序链表中的重复元素 remove-duplicates-from-sorted-list

84.柱状图中最大的矩形 largest-rectangle-in-histogram

85.最大矩形 maximal-rectangle

86.分隔链表 partition-list

87.扰乱字符串 scramble-string

88.合并两个有序数组 merge-sorted-array

89.格雷编码 gray-code

90.子集II subsets-ii

91.解码方法 decode-ways

92.反转链表II reverseLinkIist

93.复原 IP 地址 restore-ip-addresses

94.二叉树的中序遍历 binary-tree-inorder-traversal

95.不同的二叉索引搜索树 unique-binary-search-trees-ii

96.不同的二叉搜索树 unique-binary-search-trees

97.