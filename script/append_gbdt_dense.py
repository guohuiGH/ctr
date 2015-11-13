#######################################################
# File Name: append_gbdt_dense.py
# Author: guohui
# mail:
# Created Time: Thu 11 Nov 2015 21:49:34 UTC
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


def maxlen(features):
    column = len(features[0])
    ma = list()
    for col in range(0,column):
        maxValue = max([int(float(fe[col])) for fe in features])
        ma.append(maxValue)
    return ma

def append_data(file_name, max_len, origin_feature, gbdt_feature):
    f = open(file_name, 'w+')
    length = len(origin_feature)

    for i in range(0, length):
        origin_list = origin_feature[i]
        size = len(origin_list)
        for j in range (1,size):
            origin_list[j] = str(max_len[j] + int(float(origin_list[j])) + 1) + ":1"

        gbdt_list = gbdt_feature[i]
        s = len(gbdt_list)
        for j in range(1, s):
            gbdt_list[j] = str(max_len[j+size-1] + int(float(gbdt_list[j])) + 1) + ":1"
        temp_list = list()
        temp_list.extend(origin_list)
        temp_list.extend(gbdt_list[1:])
        f.write(' '.join(temp_list) + '\n')
    f.close()


def write_file():
    (train_origin_feature, train_gbdt_feature) = read_file('../tmp/aua_train', '../tmp/train_gbdt_out')
    train_len = maxlen(train_origin_feature)
    train_len.extend(maxlen(train_gbdt_feature)[1:])

    (test_origin_feature, test_gbdt_feature) = read_file('../tmp/aua_test', '../tmp/test_gbdt_out')
    test_len = maxlen(test_origin_feature)
    test_len.extend(maxlen(test_gbdt_feature)[1:])

    temp_len = max(train_len, test_len)
    sum_len = 0
    max_len = list()
    for i in range(0, len(temp_len)):
        max_len.append(sum_len)
        sum_len += (temp_len[i] + 1)

    print max_len
    append_data('../tmp/train_dense', max_len, train_origin_feature, train_gbdt_feature)
    append_data('../tmp/test_dense', max_len, test_origin_feature, test_gbdt_feature)

if __name__=='__main__':
    write_file()
