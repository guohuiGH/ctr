import os

def read_file():
    lines = open("../tmp/avazu_sample_user",'r').readlines()
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
    fptr = open("../tmp/avazu_sample_user_after_delete",'w')
    for key in dic:
        fptr.write("%s,%s\n" %(key,dic[key]))

    fptr.close()

if __name__ == "__main__":
    dic = read_file()
    write_file(dic)
