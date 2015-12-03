#!/usr/bin/python  
# -*- coding:utf8 -*- 
import os
import sys
def getFileName(path):
	dir_list = list()
	file_list = list()

	files = os.listdir(path)
	
	for f in files:
		dir_list.append(f)
	for f2 in dir_list:
		new_path = path+ "/" + f2
		new_files = os.listdir(new_path)
		for f in new_files:
			if f2 >= sys.argv[1] and f2 <= sys.argv[2]:
				file_name.write(new_path + "/" + f + "\n")
			#print f

if __name__ == '__main__':
	file_name = open("/home/ec2-user/fmg-sysu/ctr/tmp/adlog_name", "w+")
	getFileName("/home/ec2-user/fmg-sysu/adlog-data")
	file_name.close()

	file_name = open("/home/ec2-user/fmg-sysu/ctr/tmp/eventlog_name", "w+")
	getFileName("/home/ec2-user/fmg-sysu/eventlog-data")
	file_name.close()
