import os
import sys
print(sys.getdefaultencoding())

fp=open(r'D:\Git\show-me-the-code\0006\test0006.txt',encoding='utf-8')
content=fp.read()
fp.close()

print(content)
