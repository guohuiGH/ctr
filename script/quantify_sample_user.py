#######################################################
# File Name: fix_sample_user.py
# Author: guohui
# mail:
# Created Time: Mon 1 Nov 2015 16:32:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

myfile = open('../tmp/avazu_sample_user')
lines = myfile.readlines()
user_list = dict()
count = 0
users = list()
for line in lines:
    line_list = line.strip().split(',')
    if line_list[1] not in user_list:
        user_list[line_list[1]] = count
        count +=1
    line_list[1] = str(user_list[line_list[1]])
    users.append(line_list)
myfile.close()

newfile = open('../tmp/avazu_sample_user2', 'w+')
for line in users:
    newfile.write(','.join(line) + '\n')
newfile.close()

