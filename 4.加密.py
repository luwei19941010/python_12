#-*-coding:utf-8-*-
# Author:Lu Wei
import hashlib
# obj=hashlib.md5()
# obj.update('123'.encode('utf-8'))
# result=obj.hexdigest()
# print(result)

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

# obj=hashlib.md5('asd'.encode())
# obj.update('123'.encode())
# obj.hexdigest












obj=hashlib.md5('asd'.encode('utf-8'))
obj.update('asd'.encode('utf-8'))
sec=obj.hexdigest()














