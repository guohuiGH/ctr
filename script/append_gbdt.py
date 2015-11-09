#######################################################
# File Name: append_gbdt.py
# Author: guohui
# mail:
# Created Time: Thu 5 Nov 2015 16:32:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

def read_file(file_name1, file_name2):
    file1 = open(file_name1);
    file2 = open(file_name2);
    lines1 = file1.readlines()

    origin_feature = [line.strip().split(' ') for line in lines1]
    lines2 = file2.readlines()
    gbdt_feature = [line.strip().split(' ') for line in lines2]
    file1.close()
    file2.close()
    return origin_feature, gbdt_feature

def append_data(file_name, origin_feature, gbdt_feature):
    f = open(file_name, 'w+')
    length = len(origin_feature)

    for i in range(0, length):
        origin_list = origin_feature[i]
        size = len(origin_list)
        for j in range (1,size):
            origin_list[j] = str(j) + ":" + origin_list[j]
        gbdt_list = gbdt_feature[i]
        s = len(gbdt_list)
        for j in range(1, s):
            gbdt_list[j] = str(size+j) + ":" + gbdt_list[j]
        temp_list = list()
        temp_list.extend(origin_list)
        temp_list.extend(gbdt_list[1:])
        f.write(' '.join(temp_list) + '\n')
    f.close()


if __name__ == "__main__":
    (origin_feature, gbdt_feature) = read_file('../tmp/aua_train', '../tmp/train_gbdt_out')
    append_data('../tmp/train', origin_feature, gbdt_feature)

    (origin_feature, gbdt_feature) = read_file('../tmp/aua_test', '../tmp/test_gbdt_out')

    append_data('../tmp/test', origin_feature, gbdt_feature)
