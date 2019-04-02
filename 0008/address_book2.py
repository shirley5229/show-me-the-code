#coding=utf-8

import argparse

parser=argparse.ArgumentParser(description='address book test.')
parser.add_argument('action',choices=['show','add'],default='add',help='add or show address.')
parser.add_argument('-n','--name',help='Name of your friend.')
parser.add_argument('-p','--phone',help='Phone num of your friend.')

args=parser.parse_args()
if args.action=='add':
    if args.name==None:
        parser.error('Name is required')
    if args.phone==None:
        parser.error('Phone is required')

    f=open('address_book.txt','a')
    f.write('Name:{0} Phone:{1}\n'.format(args.name,args.phone))
    f.close()
    print('success!')
else: 
    #show命令，输入其他命令自动提示错误
    f=open('address_book.txt','r')
    print(f.read())
    f.close()
