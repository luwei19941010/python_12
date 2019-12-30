#-*-coding:utf-8-*-
# Author:Lu Wei


# def func(name):
# 	def inner():
# 		print(name)
# 	return inner
# v=func('luwei')

def my_func(*args):
    fs = []
    for i in range(3):
        def func():
            return i * i
        fs.append(func)#[func,func,func]
    return fs

fs1,fs2,fs3 = my_func()
print (fs1())
print (fs2())
print (fs3())