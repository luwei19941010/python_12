#-*-coding:utf-8-*-
# Author:Lu Wei

def shop_list():
    with open('goods.txt', mode='r', encoding='utf-8') as f:
        while True:
            print('欢迎使用LW的购物商场【商品管理】【查看商品列表】\n'.center(30, '*'))
            l_look=[]
            for i in f:
                l_look.append(i.strip())
            shop_length=len(l_look)
            page,a=divmod(shop_length,3)
            if a>0:
                page+=1
            while True:
                user_page=input('请输入查看的页码：1至%s页:'%(page,))
                if user_page.upper()=='N':
                    return
                print(user_page)
                if int(user_page)<=0 or int(user_page)>page:
                    print('页码输入错误请重新输入')
                else:
                    start_page=(int(user_page)-1)*3
                    end_page=int(user_page)*3
                    for info in l_look[start_page:end_page]:
                        print(info)

def shop_key():
    with open('goods.txt', mode='r', encoding='utf-8') as f:
        while True:
            print('欢迎使用LW的购物商场【商品管理】【根据关键字搜索】\n'.center(30, '*'))
            l_key = []
            user_key = input('''请输入要查询的关键字（输入N返回上一级）''').upper()
            if user_key=='N':
                return
            print('搜索结果如下'.center(20,'*'))
            for i in f:
                l_key.append(i.strip())
            for info_key in l_key:
                if user_key in info_key:
                    print(info_key)

def shop_input():
    l_input=[]
    with open('goods.txt', mode='a', encoding='utf-8') as f:
        while True:
            print('欢迎使用LW的购物商场【商品管理】【录入商品】'.center(30, '*'))
            shop_name=input('请输入商品名称（输入N返回上一级):')
            if shop_name.upper()=='N':
                return
            shop_price=input('请输入商品价格:')
            shop_num=input('请输入商品数量:')
            # d_input ={'shop_name':shop_name,'shop_price':shop_price,'shop_num':shop_num}
            # l_input.append(d_input)
            data="%s %s %s\n"%(shop_name,shop_price,shop_num)
            f.write(data)
            f.flush()#将内存里面的数据实时强行写入txt文件中。

def shop_mgmt():
    d = {'1': shop_list, '2': shop_key,'3':shop_input}
    while True:
        print('欢迎使用LW的购物商场【商品管理】'.center(30, '*'))
        user1_choice = input('''
        1.查看商品列表
        2.根据关键字搜索指定商品
        3.录入商品

        请选择（输入N返回上一级）
        请输入:''').upper()
        if user1_choice.upper()=='N':
            return
        func=d.get(user1_choice)
        func()

def vip_mgmt():
    print('此功能不可用，正在开发中，请重新选择\n')
    return


def login():
    d = {'1': shop_mgmt, '2': vip_mgmt}
    while True:
        print('欢迎使用LW的购物商场'.center(30, '*'))
        user_choice = input('''
            1.商品管理
            2.会员管理（不可选，正在开发中）
    
            请选择（输入N返回上一级）
            请输入:''')
        if user_choice.upper()=='N':
            return '退出'
        func=d.get(user_choice)
        func()

print(login())
