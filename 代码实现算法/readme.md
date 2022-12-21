# 常见python解法

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

深度优先搜索：stack

广度优先搜索：queue

二分搜索：有序列表中折中搜索

分治法：分桶


##  leetcode解法
链表，图，二叉树等等概念，都是C/C++等面向过程语言提出来的指针概念，但是python是面向对象的语言，对象==对指针进行高级封装。莫要痴迷这个东西，只要能实现结果，剩下的就是优化算法，提高效率了。

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

61.