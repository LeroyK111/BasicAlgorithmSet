#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
双向链表：每个节点有 prev 和 next
循环链表：最后一个节点的 next 指向头部\
    
    
不是查找, 而是增删改速度快.

查找是o的速度.
"""


class Node:
    def __init__(self, value):
        # 这是单向链表
        self.value = value
        self.next = None  # 指向下一个节点


class LinkedList:
    def __init__(self):
        self.head = None  # 初始链表为空

    def append(self, value):
        new_node = Node(value)
        if not self.head:  # 如果链表为空
            self.head = new_node
            return
        current = self.head
        while current.next:  # 遍历到最后一个节点
            current = current.next
        current.next = new_node  # 添加新节点

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next  # 跳过当前节点
                else:
                    self.head = current.next  # 删除头节点
                return
            prev = current
            current = current.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 输出: 1 -> 2 -> 3 -> None

ll.delete(2)
ll.display()  # 输出: 1 -> 3 -> None
