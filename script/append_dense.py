#######################################################
# File Name: append_gbdt_dense.py
# Author: guohui
# mail:
# Created Time: Thu 11 Nov 2015 21:49:34 UTC
######################################################
#!/bin/bash
#coding=utf-8
import sys
def read_file(file_name1, file_name2):
    file1 = open(file_name1);
    file2 = open(file_name2);
    lines1 = file1.readlines()

    origin_feature = [line.strip().split(' ') for line in lines1]
    lines2 = file2.readlines()
    all_feature = [line.strip().split(' ') for line in lines2]
    user_feature = [line[0:7] for line in all_feature]
    category_feature = [line[7:] for line in all_feature]
    for i in range(0, len(category_feature)):
        for j in range(0, len(category_feature[i])):
            category_feature[i][j] = int(category_feature[i][j])
    file1.close()
    file2.close()

    return origin_feature, user_feature, category_feature


def maxlen(features):
    column = len(features[0])
    ma = list()
    for col in range(1,column):
        maxValue = max([int(float(fe[col])) for fe in features])
        ma.append(maxValue)
    return ma

def append_data(file_name, max_len, user_index, origin_feature, user_feature, category_feature):
    f = open(file_name, 'w+')
    length = len(origin_feature)

    for i in range(0, length):
        origin_list = origin_feature[i] 
        userid = origin_list[1]
        size = len(origin_list)
        for j in range (1,size):
            origin_list[j] = str(max_len[j-1] + int(float(origin_list[j])) + 1) + ":1"
        

        #print origin_list
        index = user_index[userid]
        user_list = user_feature[index][:]
        category = category_feature[index][:]

        category.sort()



        s = len(user_list)
        for j in range(1, s):
            user_list[j] = str(max_len[j+size-2] + int(float(user_list[j])) + 1) + ":1"

        category_length = max_len[s+size-2]-max_len[s+size-3]
        category_list = list()

        for ca in category:
            category_list.append(str(max_len[s+size-2] + 1 + int(ca)) + ":1")


        temp_list = list()
        if sys.argv[1]=='1':
            temp_list.extend(origin_list)
        else:
            temp_list.append(origin_list[0])
            temp_list.extend(origin_list[3:])
        temp_list.extend(user_list[1:])
        temp_list.extend(category_list)
        f.write(' '.join(temp_list) + '\n')
    f.close()

def find_user(user_feature):
    user_dic = dict()
    
    for i in range(0, len(user_feature)):
        user_id = user_feature[i][0]
        user_dic[user_id] = i

    return user_dic


def write_file():
    (train_origin_feature, train_user_feature, train_category_feature) = read_file('../tmp/aua_train', '../tmp/user_feature')
    train_len = maxlen(train_origin_feature)
    #not for the userid
    train_len.extend(maxlen(train_user_feature))

    train_category = max([max(line) for line in train_category_feature])

    (test_origin_feature, test_user_feature, test_category_feature) = read_file('../tmp/aua_test', '../tmp/user_feature')
    test_len = maxlen(test_origin_feature)
    test_len.extend(maxlen(test_user_feature))
    test_category = max([max(line) for line in test_category_feature])
    
    max_category = max(train_category, test_category) 

    temp_len = max(train_len, test_len)
    temp_len.append(max_category)

    sum_len = 0
    max_len = list()

    for i in range(0, len(temp_len)):
        max_len.append(sum_len)
        sum_len += (temp_len[i] + 1)
    max_len.append(sum_len)
    print max_len

    user_index = find_user(train_user_feature)
    append_data('../tmp/train_dense', max_len, user_index, train_origin_feature, train_user_feature, train_category_feature)
    user_index = find_user(test_user_feature)
    append_data('../tmp/test_dense', max_len, user_index, test_origin_feature, test_user_feature, test_category_feature)

if __name__=='__main__':
    write_file()
