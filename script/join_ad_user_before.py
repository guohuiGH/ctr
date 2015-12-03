#Author: stone
import os

def read_ad():
    lines = open("../tmp/avazu_ad_quantify",'r').readlines()
    dic = {}
    for line in lines:
        inf = line.strip().split("@")
        key = inf[0]
        if key not in dic:
            dic[key] = inf

    return dic

def join():
    lines = open("../tmp/avazu_sample_user",'r').readlines()
    fptr = open("../tmp/avazu_ad_user_original",'w')
    dic = read_ad()
    for line in lines:
        inf = line.strip().split(",")
        key = inf[0]
        if key in dic:
            fptr.write("{}@".format("@".join(dic[key])))
            fptr.write("{}\n".format("@".join(inf[1:])))

if __name__ == "__main__":
    join()
