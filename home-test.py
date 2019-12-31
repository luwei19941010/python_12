#-*-coding:utf-8-*-
# Author:Lu Wei

# l_input = []
# while True:
#     print('欢迎使用LW的购物商场【商品管理】【录入商品】'.center(30, '*'))
#     shop_name = input('请输入商品名称（输入N返回上一级):')
#     if shop_name.upper() == 'N':
#         pass
#     shop_price = input('请输入商品价格:')
#     shop_num = input('请输入商品数量:')
#     d_input = {'shop_name': shop_name, 'shop_price': shop_price, 'shop_num': shop_num}
#     l_input.append(d_input)
#     print(d_input.values())

l_look = []
with open('goods.txt', mode='r', encoding='utf-8') as f:
    for i in f:
        l_look.append(i)
    print(len(l_look))