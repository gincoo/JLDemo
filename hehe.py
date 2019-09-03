# coding=utf-8

class Demo:

    def __init__(self,name):
        self.name = name
        print('init---%s :'% name)

    def __del__(self):
        print('del---')

    def __str__(self):
        return '123'

hehe = Demo('guagua')
print(hehe)
del hehe