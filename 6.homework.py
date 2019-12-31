#-*-coding:utf-8-*-
# Author:Lu Wei

#1.写出三元运算的基本格式及作用？
# a=1
# b=2
# v= a if a>b else b
# print(v)

#2.什么是匿名函数？
#lambda
# x=100
# v=lambda x:x+100
# print(v(100))

#3.内置函数
#其他 id type open range len
#强制转换 list str int tuple set（） dict bool
#数学相关 max sum min divmod abs() float
#输入输出 print input
#进制转换 bin(0b) oct(0o) int hex(0x)
#chr()unicode编码找字符串     ord()字符串找unicode 编码  map  filter functools.reduce

#4.filter/map/reduce函数的作用分别是什么？
#filter(x,y) 删选 x为函数 y可迭代参数 list tuple str set（）
#map(x,y) d多对多 x为函数 y可迭代参数 list tuple str set（）
#reduce 求和

#5.看代码写结果
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# # a. 执行 func(12,3,*[11,22]) ，输出什么？
# func(12,3,*[11,22])
# # (12,3,11,12)
# # b. 执行 func(('alex','武沛齐',),name='eric')
# func(('alex','武沛齐',),name='eric')
# #(('alex','武沛齐',),{'name':'eric'))

#6.看代码分析结果

# def func(arg):
#     return arg.pop(1)
#
# result = func([11,22,33,44])
# print(result)#22

#7.看代码分析结果
# def lda():
#     return i
# func_list = []
# for i in range(10):
#     func_list.append(lambda :i)
# print(func_list)
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1,v2)#9,9
# #变形
# func_list = []
# for i in range(10):
#     func_list.append(lambda i:i)
# print(func_list)
# v1 = func_list[0](0)
# v2 = func_list[5](5)
# print(v1,v2)#0,5


#8.看代码分析结果
#
# def lda(x):
#     return x+i
#
# func_list = []
# for i in range(10):
#     func_list.append(lambda x:x+i)
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1,v2)#11,10

#9.看代码分析结果
#
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x:x+i)#i=9
#
# for i in range(0,len(func_list)):#(0,10)
#     result = func_list[i](i)#0,1,2,3,4,5,6,7,8,9
#     print(result)
# #result=0,2,4,6,8,10,12,14,16,18

#10.看代码分析结果
#
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#     return f1
#
# func = f2()#print('f2')
# result = func()#print('f1')
# print(result)#None



#11.看代码分析结果【面试题】
#
# def f1():
#     print('f1')
#     return f3()#None
# def f2():
#     print('f2')
#     return f1
# def f3():
#     print('f3')
#
# func = f2()
# result = func()
# print(result)
# '''
# 'f2'
# 'f1'
# 'f3'
# None
# '''

#12.看代码分析结果
#
# name = '景女神'
# def func():
#     def inner():
#         print(name)
#     return inner()
# v = func()
# print(v)
# '''
# 景女神
# None
# '''


#13.看代码分析结果

# name = '景女神'
# def func():
#     def inner():
#         print(name)
#         return "老男孩"
#     return inner()
# v = func()
# print(v)
# '''
# 景女神
# 老男孩
# '''

#14.看代码分析结果
#
# name = '景女神'
# def func():
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
# v = func()#inner
# result = v()#
# print(result)#
# '''
# 景女神
# 老男孩
# '''

#15.看代码分析结果

# def func():
#     name = '武沛齐'
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
# v1 = func()
# v2 = func()
# print(v1,v2)
# #inner inner 内存地址

#16.看代码写结果

# def func(name):
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v1 = func('金老板')
# v2 = func('alex')
# print(v1,v2)
#inner inner 内存地址

#17.
# def func(name=None):
#     if not name:
#         name= '武沛齐'
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v1 = func()#inner 内存地址
# v2 = func('alex')#inner 内存地址
# print(v1,v2)


#18.看代码写结果【面试题】

# def func(name):
#     v = lambda x:x+name
#     return v
#
# v1 = func('武沛齐')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1,v2,v3,v4)
# #v内存地址,v内存地址,银角武沛齐,金角alex


#19.看代码写结果

# NUM = 100
# result = []
# for i in range(10):
#     func = lambda : NUM      # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)#9
# print(result)#[10个func的内存地址]
# v1 = result[0]()#100
# v2 = result[9]()#100
# print(v1,v2)


#21.看代码分析结果【面试题】
#
# def func(num):
#     def inner():
#         print(num)
#     return inner
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)#9
# print(result)#[inner,inner...inner]
# v1 = result[0]()#0
# v2 = result[9]()#9
# print(v1,v2)

