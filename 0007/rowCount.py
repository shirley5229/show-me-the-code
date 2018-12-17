# -*- coding: utf-8 -*-
import os
'''
统计Python项目下的代码行数
'''
COUNT = 0
def rowCount(path):
	global COUNT
	for i in os.listdir(path):
		#print(i)   #获得当前目录下文件名称
		fullpath=path+os.sep+i
		if os.path.isdir(fullpath):
			rowCount(fullpath)
		else:
			if i[-3:]=='.py':
				fp=open(fullpath,'r',encoding='utf-8')
				code=fp.readlines()
				#print(len(code))
				COUNT=COUNT+len(code)
	return COUNT

count1=rowCount(r"D:\Git\pyrequest\tms3_rest_test")
print("代码总行数："+str(count1))
