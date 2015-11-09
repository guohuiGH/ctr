#######################################################
# File Name: split_data.py
# Author: guohui
# mail:
# Created Time: Thu 5 Nov 2015 16:32:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

input_file = open('../tmp/aua_feature')

train_file = open('../tmp/aua_train', 'w+')
test_file = open('../tmp/aua_test', 'w+')

lines = input_file.readlines()
count = 0
for line in lines:
    line_list = line.strip().split(' ')
    new_line = list()
    new_line.append(line_list[0])
    new_line.extend(line_list[3:])
    l = ' '.join(new_line) + '\n'
    if count % 5 == 0:
        test_file.write(l)
    else:
        train_file.write(l)
    count +=1
input_file.close()
train_file.close()
test_file.close()


