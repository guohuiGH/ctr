#Author: zhangyan
import os

if __name__ == "__main__":
    lines = open("../tmp/avazu_user_quantify",'r').readlines()
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
    fptr = open("../tmp/avazu_sample_user",'w+')
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
                fptr.write("%s\n" %line)
                sum_none -= 1



