#-*-coding:utf-8-*-
# Author:Lu Wei

import random

def get_random_code(length=6):
    data=[]
    for i in range(length):
        v=random.randint(65,90)
        data.append(chr(v))
    return ''.join(data)
print(get_random_code(3))

v='中'
print(v)

v=chr(65)
print(v)









def hash_data(len):
    l=[]
    for i in range(len):
        v=random.randint(65,90)
        l.append(chr(v))
    return ''.join(l)

get_hash_code=hash_data(6)
print(get_hash_code)


l1=[1,2,3,4,'asd','asd']
l2=[1,3,4,5,6]
#
# v1=map(lambda x:x+100,l1)
# print(list(v1))
#
# v2=filter(lambda x:type(x)==str,l1)
# print(list(v2))



import functools
v3=functools.reduce(lambda x,y:x+y,l2)
print(v3)