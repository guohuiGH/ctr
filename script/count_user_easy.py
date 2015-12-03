import os

def statistic():
    lines = open("../tmp/aua_feature",'r').readlines()
    dic = {}
    for line in lines:
        inf = line.strip().split(' ')
        label = inf[0]
        key = inf[1]
        if label == "1" and key not in dic:
            dic[key] = 1
        elif label == "1" and key in dic:
            dic[key] += 1
    print len(dic)
    #for key in dic:
     #   print str(dic[key]) + ' '+key

if __name__ == "__main__":
    statistic()

