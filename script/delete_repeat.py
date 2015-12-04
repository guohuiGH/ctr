import os
import sys


if sys.argv[1]=='1':
    input_name = '../data/test/avazu_sample_user'
    write_name = '../data/test/avazu_sample_user_after_delete'
elif sys.argv[1]=='0':
    input_name = '../data/train/avazu_sample_user'
    write_name = '../data/train/avazu_sample_user_after_delete'
def read_file():
    global input_name
    lines = open(input_name,'r').readlines()
    dic = {}
    for line in lines:
        inf = line.strip().split(',')
        key = inf[0]+','+inf[1]
        if key not in dic:
            dic[key] = inf[2]
        else:
            if dic[key] == "0" and inf[2] == "1":
                dic[key] = inf[2]

    return dic


def write_file(dic):
    global write_name
    fptr = open(write_name,'w')
    for key in dic:
        fptr.write("%s,%s\n" %(key,dic[key]))

    fptr.close()

if __name__ == "__main__":
    dic = read_file()
    write_file(dic)
