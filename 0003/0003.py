# -*- coding: utf-8 -*-
import os
'''
统计Python项目下的代码行数
'''
path=r'D:\Git\senyint_tms3 release\tms3\test_case'
COUNT = 0
for root,dirs,files in os.walk(path):
	#print(files)   #files是列表
	for f in files:
		if f[-3:]=='.py':
			COUNT=COUNT +1
print("文件总数："+str(COUNT))
