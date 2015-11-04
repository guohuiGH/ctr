#!/usr/bin/python  
# -*- coding:utf8 -*- 

#Author:guohui

def read_ad_binary():
    ad_file = open("../tmp/avazu_ad_binary", "r")
    lines = ad_file.readlines()
    ad_list = list()
    for line in lines:
        ad_list.append(line.strip("\n"))
    ad_file.close()
    return ad_list

def read_user():
    user_file = open("../tmp/avazu_sample_user", "r")
    lines = user_file.readlines()
    user_list = list()
    for line in lines:
        line_list = line.strip("\n").split(",")
        user_list.append(line_list)
    user_file.close()
    max_user_length = len(bin(max(map(int, [line[0] for line in user_list])))[2:])
    return user_list, max_user_length

def join_function():
    join_file = open("../tmp/avazu_user_ad_binary", "w+")
    ad_list = read_ad_binary()

    user_list, max_user_length = read_user()
    result = ""
    count_total = 0
    count_click = 0
    for user_action in user_list:
        result = bin(int(user_action[1]))[2:].zfill(max_user_length) + ad_list[int(user_action[0])] +"ss"+ user_action[2]
        join_file.write(result + "\n")
        count_total +=1
        if user_action[2] == '1':
            count_click+=1
    join_file.close()
    print count_click
    print count_total

if __name__ == '__main__':
    join_function()