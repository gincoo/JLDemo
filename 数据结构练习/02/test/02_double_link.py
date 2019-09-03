# coding=utf-8

class Node(object):

    # 双向链表节点
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class DLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur_node = self.__head
        count = 0
        while cur_node.next != None:
            count += 1
            cur_node = cur_node.next
        return count

    def add(self, item):
        """头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.pre = node

    def append(self,item):
        """尾部添加"""



