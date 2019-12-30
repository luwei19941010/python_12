#-*-coding:utf-8-*-
# Author:Lu Wei


'''
v1=[11,22,33,44]
def func(arg):
    print()
#第一个参数：必须是一个函数
#第二个参数：必须是一个可迭代类型（list，str,tuple,set())
v1=[11,22,33,44]
result=map(lambda x:x+100,v1)
print(result)#py2 111,122,133,144
print(list(result))#py3 111,122,133,144



v1=[11,22,33,44,'asd','ac']
result=filter(lambda x:type(x)==int,v1)
print(list(result))
'''

import functools
# v1=[11,22,33,44]
#
# def func(x,y):
#     return x+y
# result=functools.reduce(func,v1)
# print(result)

# v1=['a','asd','qwe','fdg']
# result=functools.reduce(lambda x,y:x+y,v1)
# print(result)








