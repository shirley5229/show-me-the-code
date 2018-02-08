#!/usr/bin/env python
# encoding: utf-8
__author__ = 'MX'

import os,re

def findString(filePath, regex):
	dictResult = {}
	fileObj = open(filePath, 'r')

	for line in fileObj.readlines():
		#获取当前行的所有单词
		listMatch = re.findall('[a-zA-Z]+', line.lower())
		#每个单词出现的次数，存入字典dictResult
		for eachLetter in listMatch:
			#存入字典，如果单词已经出现过，则在原基础上+1
			dictResult[eachLetter] = dictResult.get(eachLetter, 0) + 1
		#print(dictResult)

	#根据单词首字母，对字典排序
	result = sorted(dictResult.items(),key = lambda x:x[0][0])
	for each in result:
		print(each)
	
findString("0004.txt",'William')

