#######################################################
# File Name: gbdt_feature_append_test.py
# Author: guohui
# mail:
# Created Time: Sat 12 Nov 2015 19:32:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

is_user_ad = 1

def write_file(file_name1, file_name2):
    global is_user_ad
    input_file = open(file_name1)
    output_file = open(file_name2, 'w+')

    lines = input_file.readlines()
    count = 0
    for line in lines:
        line_list = line.strip().split(' ')
        new_line = list()
        new_line.append(line_list[0])
        new_line.extend(line_list[is_user_ad:])
        l = ' '.join(new_line) + '\n'
        output_file.write(l)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    write_file('../tmp/aua_feature', '../tmp/aua_train')
    write_file('../tmp/test_aua_feature', '../tmp/aua_test')



