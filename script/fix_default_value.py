#######################################################
# File Name: fix_default_value.py
# Author: guohui
# mail:
# Created Time: Sat 31 Oct 2015 16:32:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

import math
def read_file():
    ad_file = open("../tmp/avazu_ad_quantify")
    ad_list = list()
    for line in ad_file.readlines():
        line_list = line.strip("\n").split("@")
        ad_list.append(line_list)
    
    user_file = open("../tmp/avazu_sample_user2")
    user_ad_list = [[]]
    download_list = [[]]
    count_user = 0; count_download = 0
    for line in user_file.readlines():
        line_list = line.strip("\n").split(",")

        user_ad_list[count_user].append(line_list[2])
        user_ad_list[count_user].append(line_list[1])
        user_ad_list[count_user].extend(ad_list[int(line_list[0])])
        user_ad_list.append(list())
        count_user += 1
        if (int(line_list[2]) == 1 ):
            download_list[count_download].append(line_list[2])
            download_list[count_download].append(line_list[1])
            download_list[count_download].extend(ad_list[int(line_list[0])])
            download_list.append(list())
            count_download += 1

    ad_file.close()
    user_file.close()
    len_d = len(download_list)
    len_u = len(user_ad_list)
    return ad_list,download_list[:len_d-1], user_ad_list[:len_u-1]

def find_default_value(input_list):
    default_value = list()
    size = len(input_list[0])
    install_dict = dict(); star_dict = dict()
    view_avg = list(); size_avg = list()
    for line in input_list:
        if line[size-4] != '-1' and line[size-4] not in install_dict:
            install_dict[line[size-4]] = 1
        elif line[size-4] != '-1':
            install_dict[line[size-4]] += 1

        if line[size-3] != '-1' and line[size-3] not in star_dict:
            star_dict[line[size-3]] = 1
        elif line[size-3] != '-1':
            star_dict[line[size-3]] +=1

        if line[size-2] != '-1':
            view_avg.append(float(line[size-2]))

        if line[size-1] != '-1':
            size_avg.append(float(line[size-1]))

    items = install_dict.items()
    new_items = [[v[1],v[0]] for v in items] 
    new_items.sort()
    default_value.append(new_items[len(new_items)-1][1])

    items = star_dict.items()
    new_items = [[v[1], v[0]] for v in items]
    new_items.sort()
    default_value.append(new_items[len(new_items)-1][1])

    default_value.append(round(sum(view_avg) / len(view_avg)))
    default_value.append(round(sum(size_avg) / len(size_avg)))
    view_avg.sort()
    #default_value.append(view_avg[len(view_avg)/2])
    size_avg.sort()
    #default_value.append(size_avg[len(size_avg)/2])
    print default_value
    return default_value




def fix_default_list(default_download_value, default_ad_value):
    fixed_list = list()
    size = len(user_ad_list[0])
    for line in user_ad_list:
        for i in range(1,5):
            if line[0] == '1' and line[size-i] == '-1':
                line[size-i] = default_download_value[4-i]
            elif line[0] == '0' and line[size-i] == '-1':
                line[size-i] = default_ad_value[4-i]
        fixed_list.append(line)
    return fixed_list


def normalizaling_feature():
    normalization_list = list()

    size = len(fixed_list[0])
    for line in fixed_list:
        #deal with install, views, size
        installs = ''.join(line[size-4].split(',')).split(' - ')
        line[size-4] = str(round(math.log((int(installs[0]) + int(installs[1]) /2)) / math.log(10)))
        line[size-2] = str(round(math.log(int(line[size-2]))/ math.log(10)))
        s = float(line[size-1])
        if (s > 100):
            s = 100
        elif (s < 0.1):
            s = 0.1
        line[size-1] = str(s)
        normalization_list.append(line)
    return normalization_list

def write_file(normalization_list):
    myfile = open("../tmp/aua_feature", "w+")
    for line in normalization_list:
        myfile.write(','.join(line) + '\n')
    myfile.close()

        
        

if __name__ == "__main__":
    (ad_list, download_list, user_ad_list) = read_file()
    default_download_value = find_default_value(download_list)
    default_ad_value = find_default_value(user_ad_list);
    fixed_list = fix_default_list(default_download_value, default_ad_value)
    normalization_list = normalizaling_feature()
    write_file(normalization_list)

