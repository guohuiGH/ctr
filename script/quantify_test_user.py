#########################################################################
#    > File Name: quantify_test_user.py
#    > Author: 
#    > Mail: 
#    > Created Time: Fri 13 Nov 2015 12:08:26 PM UTC
# ************************************************************************/
#coding=utf-8

def read_ad_file():
    map_ad_file = open('../tmp/avazu_map_ad')
    line = map_ad_file.readline()
    map_ad = dict()
    while line:
        line_list = line.strip().split(',')
        map_ad[line_list[0]] = line_list[1]
        line = map_ad_file.readline()
    map_ad_file.close()
    return map_ad

def read_user_file():
    map_user_file = open('../tmp/avazu_map_user')
    line = map_user_file.readline()
    map_user = dict()
    reverse_map_user = dict()
    while line:
        line_list = line.strip().split(',')
        map_user[line_list[0]] = line_list[1]
        reverse_map_user[line_list[1]] = line_list[0]
        line = map_user_file.readline()
    map_user_file.close()

    sample_user_file = open('../tmp/avazu_sample_user')
    sample_user_list = [line.strip().split(',')[1] for line in sample_user_file.readlines()]
    sample_user_file.close()

    sample_user = dict()
    for user in sample_user_list:
        sample_user[reverse_map_user[user]] = user
    print len(sample_user)
    return sample_user

def read_test_user(map_ad, map_sample_user):
    test_user_file = open('../tmp/test_avazu_user_info')
    test_user_quantify_file = open('../tmp/avazu_user_test_quantify', 'w+')
    user_key = map_sample_user.keys()
    ad_key = map_ad.keys()
    line = test_user_file.readline()
    count = 0; count_invalid_ad = 0; count_invalid = 0
    while line:
        temp_line = ''
        count += 1
        line_list = line.strip().split('@@')

        if line_list[1] not in user_key:
            line = test_user_file.readline()
            count_invalid += 1
            continue
        if line_list[0] not in ad_key:
            line = test_user_file.readline()
            count_invalid_ad +=1
            continue
        temp_line += map_ad[line_list[0]] + ','
        temp_line += map_sample_user[line_list[1]] + ','

        try:
            click_value = line_list[2]
        except:
            click_value = '2105'
            print line
        if click_value < '2104':
            temp_line += '1'
        else:
            temp_line += '0'
        temp_line += '\n'
        test_user_quantify_file.write(temp_line)
        line = test_user_file.readline()
    test_user_file.close()
    test_user_quantify_file.close()
    print count, count_invalid_ad,count_invalid
        
if __name__=='__main__':
    map_ad = read_ad_file()
    map_sample_user = read_user_file()
    read_test_user(map_ad, map_sample_user)
