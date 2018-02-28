import argparse

file_path = './data.txt'
#定义命令行的参数
parser = argparse.ArgumentParser(description='CLI address book')
parser.add_argument('action', choices=['show', 'add'], default='add', help='add or display address book')
parser.add_argument('-n', '--name', help='Name of your friend')
parser.add_argument('-p', '--phone', help='Phone number of your friend', type=int)
 #接收命令行的参数
args = parser.parse_args()
print(args)
if args.action == 'add':
    if args.name == None:
        parser.error('Name is required')
    if args.phone == None:
        parser.error('Phone is required')
    f = open(file_path, 'a')
    f.write("Name: %s\tPhone: %s\n" %(args.name, args.phone))
    print('%s saved!' %(args.name))
    f.close()
else: #show
    print(open(file_path, 'r').read())
