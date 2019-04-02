#coding=utf-8
import os

class address_book(object):
    """命令行通讯录."""
    def __init__(self):
        pass

    def add(self):
        #读写文件，将name phone写入文件中
        print('使用address_book命令添加通讯录：')
        addcmd=input( )
        data=addcmd.split('=')

        if len(data)==3 and data[0]=='address_book add -n=' and data[1][-3:]==' -p':
            name=data[1][:-3]
            phone=data[2]

            fp=open('address_book.txt','a')
            fp.write('Name:'+name+'  Phone:'+phone+'\n')
            fp.close()
            print("add success!")
        else:
            print('command error!')

    def show(self):
        showcmd=input()
        if showcmd=='address_book show':
            fp=open('address_book.txt')
            print(fp.read())
            fp.close()
        else:
            print('command error!')


if __name__=="__main__":
    ab=address_book()
    ab.add()
    ab.show()
