# File Name: join_userfeature_auafeature.py
# Author:stone 
# Mail: 
# Created Time: 2015.11.23
import os

def read_user_feature():
    dic = {}
    lines = open("../tmp/user_feature",'r').readlines()
    for line in lines:
        inf = line.strip().split(' ')
        key = inf[0]
        tmp = inf[1:]
        dic[key] = tmp

    return dic

def join_file(dic):
    lines = open("../tmp/aua_feature",'r').readlines()
    fptr = open("../tmp/aua_user_feature",'w')
    for line in lines:
        inf = line.strip().split(' ')
        key = inf[1]
        if key in dic:
            fptr.write("%s " %inf[0])
            fptr.write("{} ".format(" ".join(inf[3:])))
            fptr.write("{}\n".format(" ".join(dic[key])))
        else:
            print key
    fptr.close()

if __name__ == "__main__":
    dic = read_user_feature()
    join_file(dic)
