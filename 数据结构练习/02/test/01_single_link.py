# coding=utf-8

class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部增加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 遍历链表集合
            node_cur = self.__head
            while node_cur.next != None:
                node_cur = node_cur.next
            # 退出循环时候,cur_node 指向最后一个
            node_cur.next = node

    def length(self):
        """链表长度"""
        count = 0
        cur_node = self.__head
        while cur_node.next != None:
            count += 1
            cur_node = cur_node.next
        return count

    def travel(self):
        """遍历 打印列表"""
        cur_node = self.__head
        while cur_node.next != None:
            print(cur_node.item, end=' ')
            cur_node = cur_node.next
        print("")

    def insert(self, pos, item):
        """插入数据"""
        if pos <= 0:
            # 头部添加
            self.add(item)
        elif pos > self.length():
            # 尾部添加
            self.append(item)
        else:
            # 中间插入数据
            node = Node(item)
            cur_node = self.__head
            index = 0
            while index < (pos - 1):
                index += 1
                cur_node = cur_node.next
            # 结束后的位置为 pos-1
            node.next = cur_node.next
            cur_node.next = node

    def search(self,item):
        """是否存在"""
        cur_node = self.__head
        while cur_node.next !=None:
            if item == cur_node.item:
                return True
            cur_node = cur_node.next
        return False
