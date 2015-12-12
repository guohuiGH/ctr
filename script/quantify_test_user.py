#########################################################################
#    > File Name: quantify_test_user.py
#    > Author: 
#    > Mail: 
#    > Created Time: Fri 13 Nov 2015 12:08:26 PM UTC
# ************************************************************************/
#coding=utf-8

import sys

def read_ad_file():
    #map_ad_file = open('../data/ad/avazu_map_ad')
    #line = map_ad_file.readline()
    #map_ad = dict()
    #while line:
    #    line_list = line.strip().split(',')
    #    map_ad[line_list[1]] = line_list[0]
    #    line = map_ad_file.readline()
    #map_ad_file.close()
    return map_ad
    



def read_file():
    #map_user_file = open('../data/user/avazu_map_user')
    #line = map_user_file.readline()
    #map_user = dict()
    #reverse_map_user = dict()
    #while line:
    #    line_list = line.strip().split(',')
    #    map_user[line_list[0]] = line_list[1]
    #    reverse_map_user[line_list[1]] = line_list[0]
    #    line = map_user_file.readline()
    #map_user_file.close()

    sample_user_file = open('../data/train/avazu_sample_user_after_delete')
    lines = sample_user_file.readlines()
    sample_user_list = [line.strip().split(',')[1] for line in lines]
    ad_list = [line.strip().split(',')[0] for line in lines]
    sample_user_file.close()
    
    #sample_user = dict()
    sample_user = dict()
    for user in sample_user_list:
        #sample_user[reverse_map_user[user]] = user
        sample_user[user] = 1
    sample_ad = dict()
    for ad in ad_list:
        sample_ad[ad] = 1
    print len(sample_user), len(sample_ad)
    return sample_user, sample_ad

def read_test_user(map_ad, map_sample_user):
    test_user_file = open('../data/test/avazu_user_quantify')
    test_user_quantify_file = open('../data/test/avazu_sample_user2', 'w+')
    #user_key = map_sample_user.keys()
    #ad_key = map_ad.keys()
    line = test_user_file.readline()
    count = 0; count_invalid_ad = 0; count_invalid = 0
    count_invalid_user = dict()
    while line:

        count += 1
        line_list = line.strip().split(',')

        if line_list[1] not in map_sample_user:
            line = test_user_file.readline()
            count_invalid += 1
            continue
        count_invalid_user[line_list[1]] = 1
        if line_list[0] not in map_ad:
       #     line = test_user_file.readline()
            count_invalid_ad +=1
            #continue

        
        test_user_quantify_file.write(line)
        line = test_user_file.readline()
    test_user_file.close()
    test_user_quantify_file.close()
    print count, count_invalid_ad,count_invalid, len(count_invalid_user)
        
if __name__=='__main__':

    (map_sample_user,map_ad) = read_file()

    read_test_user(map_ad, map_sample_user)
