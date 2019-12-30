day12

### 今日内容

- 函数中高级（闭包/高阶函数）
- 内置函数
- 内置模块

### 内容回顾

- 函数作为变量

```
def func():
	pass
v1=func
v1()
```

- 函数作为参数

```
def func(arg):
	v2=arg()
def show():
	pass
v1=func(show)
#注意返回值
```

python中以函数作为作用域

lambda函数（匿名函数）

```
lambda x:x=100
```



### 详细内容

#### 1.函数中高级#

####注意#函数是由谁创建的，那么以后作用域就从谁开始找

##### 1.1函数可以做返回值

```
def func():
	print(123)
def bar():
	return func
v=bar()


name = 'oldboy'
def func():
    print(name) 
def bar():
    return func
v = bar()
v()


def bar():
    def inner():
        print(123)
    return inner
v = bar()
v()
```



```
name='oldboy'
def bar(name):
	def inner():
		print(name)
	return inner
v=bar()#{inner}
v()#{oldboy}
```

闭包

```
name='oldboy'
def bar(name):
	def inner():
		print(name)
	return inner
v1=bar('alex')#{name=alex,inner}#闭包，为内存创建一块区域（内部变量供自己使用),为他以后执行提供信息。
v2=bar('eric')#{name=eric,inner}
v1=()#alex
v2=()#eric
```



练习题

```
#1.
name='alex'
def base():
	print(name)
def func():
	name='eric'
	base()
func()# alex

#2.
name='alex'
def func():
	name='eric'
	def base():
		print(name)
	base()
func()# eric

#3.
name='alex'
def func():
	name='eric'
	def base():
		print(name)
	return base
base=func()
base()#eirc

```

面试题

```
info =[]
def func():
	print(item)
for item in range(10):
	info.append(func)#info=[func,func,func,func...func]
info[0]()#9
```

```
info =[]
def func():
	def inner():
		print(i)
	return inner
	
for item in range(10):
	info.append(func(item))#info=[[i=0,inner],[i=2,inner]...[i=9,inner]]
info[0]()#0
info[1]()#1
info[4]()#4
```



##### 1.2闭包

​		把函数传入的值导入到内存，以备未来使用。

​		简单来说就是一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行。

```
def func(name):
	def inner():
		print(name)
	return inner
v=func('luwei')
```

闭包陷阱题

```
def my_func(*args):
    fs = []
    for i in range(3):#for循环被执行
        def func():#func函数不会被执行，但是for循环一直在。
            return i * i#0,1,4
        fs.append(func)#[func,func,func]
    return fs

fs1,fs2,fs3 = my_func()
print (fs1())
print (fs2())
print (fs3())
```

##### 1.3高阶函数

- 把函数当作参数传递
- 把函数当作返回值

注意：对函数进行赋值 

##### 1.4总结

- 函数执行流程分析（函数到底是谁创建的-画图）

  ![image-20191230093136062](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191230093136062.png)

- 闭包概念：为函数中创建一块区域并为其维护自己的数据，以后执行时方便调用。【应用场景：装饰器，SQLAlchemy源码】

- 

#### 2.内置函数

- ​	编码相关

  - chr() 将十进制数字转换成unicode编码中的对应字符串。unicode 包括了ascii

    ```
    v=chr(99)
    print(v)
    ```

  - ord() 将字符串转换成unicode编码中的对应的十进制数字

    ```
    v=ord('中')
    print(v)
    ```

    应用

    ```
    import random
    
    def get_random_code(length=6):
        data=[]
        for i in range(length):
            v=random.randint(65,90)
            data.append(chr(v))
        return ''.join(data)
    print(get_random_code(3))
    ```



- 高级内置函数

  - map（x,y)，循环每个元素（第二个参数），然后让每个元素执行（第一个参数），将每个函数执行结果保存到新的列表中，并返回。

    map 有返回值。

    

    ![image-20191230134608881](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191230134608881.png)

    ​									遍历序列，对序列中每个元素进行操作，最终获取新的序列。

    案列

    ```
    map中#第一个参数：必须是一个函数
    map中#第二个参数：必须是一个可迭代类型（list，str,tuple,set())
    v1=[11,22,33,44]
    result=map(lambda x:x+100,v1)
    print(result)#py2 111,122,133,144  #py3  <map object at 0x0000000000BC5940>
    print(list(result))#py3 111,122,133,144 
    ```

  - filter(x,y)循环每个元素（第二个参数），然后让每个元素执行（第一个参数），将每个函数执行结果保存到新的列表中，并返回。

    filter 有返回值。

    ![image-20191230134643575](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191230134643575.png)

    ​								对于序列中的元素进行筛选，最终获取符合条件的序列	

  ```
  filter中#第一个参数：必须是一个函数
  filter中#第二个参数：必须是一个可迭代类型（list，str,tuple,set())
  v1=[11,22,33,44,'asd','ac']
  result=filter(lambda x:type(x)==int,v1)
  print(list(result))
  ```

  - reduce()

  ![image-20191230134814027](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191230134814027.png)

  ​														对于序列内所有元素进行累计操作

  ```
  import functools
  v1=[11,22,33,44]
  
  def func(x,y):
      return x+y
  result=functools.reduce(func,v1)
  print(result)
  
  v1=['a','asd','qwe','fdg']
  result=functools.reduce(lambda x,y:x+y,v1)
  print(result)
  ```

  

  ​										

- 面试题

  - 常用的内置函数有哪些

  - filter/map/reduce是什么意思？

  - 什么是匿名函数

    ```
    lambda x:x=100
    ```

    

#### 3.模块

- MD5

将指定的"字符串"进行加密

```
import hashlib
obj=hashlib.md5()
obj.update('123'.encode('utf-8'))
result=obj.hexdigest()
print(result)


def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result
val=get_md5('123')
print(val)
```

- 加盐

```
import hashlib
def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result
val=get_md5('123')
print(val)
```

应用

```

import hashlib,getpass

def get_md5(data):
    obj=hashlib.md5('123asd'.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result=obj.hexdigest()
    return result
def register():
    print('register'.center(40,'+'))
    while True:
        user=input('new_username:')
        if user.lower() =='n':
            return
        psd=input('new_password:')
        i={'username':user,'password':get_md5(psd)}
        l.append(i)

def login():
    print('login'.center(20,'*'))
    count = 0
    while True:
        login_user=input('login_username:')
        login_psd=input('login_password:')
        for i in l:
            if login_user==i['username'] and get_md5(login_psd)==i['password']:
                return True
            count += 1
            print(count)
            if count == 5:
                return
l = []
register()
result=login()
if result:
    print('ok')
else:
    print('no')

```



##### 密码不显示 getpass 只能在终端显示

```
import  getpass
pwd=getpass.getpass('password:')
print(pwd)
```

























