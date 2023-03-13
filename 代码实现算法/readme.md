# 常见python解法

## 数据结构

### 为什么要学习数据结构和算法？

随着应用程序变得越来越复杂和数据越来越丰富，几百万、几十亿甚至几百亿的数据就会出现，而对这么大对数据进行搜索、插入或者排序等的操作就越来越慢，数据结构就是用来解决这些问题的。

![[数据结构.png]]

常用数据结构一共有九种。

### 应用实例

**本部分由python实现，JavaScript逻辑一样。**

至于进一步加快计算过程，还需要多线程多进场协程等配合。




## 什么是算法？

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

86.