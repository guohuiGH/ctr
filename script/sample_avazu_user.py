#Author: zhangyan
#change by guohui 20151204. change the file name
import os
import sys

if __name__ == "__main__":
    if sys.argv[1]=='1':
        input_name = '../data/test/avazu_user_quantify'
        write_name = '../data/test/avazu_sample_user'
    elif sys.argv[1] == '0':
        input_name = '../data/train/avazu_user_quantify'
        write_name = '../data/train/avazu_sample_user'
    lines = open(input_name,'r').readlines()
    dic = {}
    count = 0
    sub = 0
    for line in lines:
        line = line.strip()
        ad,usr,cl = line.split(",")
        if cl == "1":
            count += 1
            
        if usr not in dic:
            if cl == "1":
                dic[usr] = [0,1]
            else:
                dic[usr] = [1,0]

        else:
            if cl == "1":
                dic[usr][1] += 1
            else:
                dic[usr][0] += 1
    fptr = open(write_name,'w+')
    sum_one = 0
    sum_zero = 0
    active = 0
    for key in dic:
        if dic[key][1] > 0:
            active += 1
            sum_one += dic[key][1]
            sum_zero += dic[key][0]

    sum_none = sum_one * 10 - sum_zero
    print len(dic)
    print active
    print sum_one
    print sum_zero
    print sum_none

    for line in lines:
        line = line.strip()
        ad,usr,cl = line.split(",")
        if dic[usr][1] > 0:
            fptr.write("%s\n" %line)
        else:
            if sum_none > 0:
                print "comein"
                fptr.write("%s\n" %line)
                sum_none -= 1



