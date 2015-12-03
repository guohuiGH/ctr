import os

def statistic():
    lines = open("../tmp/aua_feature",'r').readlines()
    dic = {}
    for line in lines:
        inf = line.strip().split(' ')
        label = inf[0]
        key = inf[1]
        if label == "1" and key not in dic:
            tmp = []
            tmp.append(1)
            a = set()
            a.add(inf[6])
            tmp.append(a)
            tmp.extend(inf[7:])
            dic[key] = tmp
        elif label == "1" and key in dic:
            count = dic[key][0]
            dic[key][0] += 1
            dic[key][1].add(inf[6])
            dic[key][2] = (float(dic[key][2])*count + float(inf[7])) / dic[key][0]
            dic[key][3] = (float(dic[key][3])*count + float(inf[8])) / dic[key][0]
            dic[key][4] = (float(dic[key][4])*count + float(inf[9])) / dic[key][0]
            dic[key][5] = (float(dic[key][5])*count + float(inf[10])) / dic[key][0]
            
    return dic

def write_file(dic):
    fptr = open("../tmp/user_feature",'w')
    print len(dic)
    for key in dic:
        fptr.write("%s %d %d " %(key,dic[key][0],len(dic[key][1])))
        #fptr.write("%s %d " %(key,len(dic[key][1])))
        for i in xrange(2,6):
            dic[key][i] = str(round(float(dic[key][i]),1))
        fptr.write("{}".format(" ".join(dic[key][2:])))
        l = list(dic[key][1])
        for index,item in enumerate(l):
            l[index] = int(item)
        l.sort()
        for c in l:
            fptr.write(" %d" %c)
        fptr.write("\n")
    fptr.close()
        




if __name__ == "__main__":
    dic = statistic()
    write_file(dic)
