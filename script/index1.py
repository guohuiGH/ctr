#!/usr/bin/env python

from datetime import datetime
# load name data
def load_name_sample(input,isTest):
    f = open(input)
    y = []
    x = []
    max_feature = 0
    field_cnt = 0
    line = f.readline()
    index = 1
    if isTest == True:
        index = 2
    cnt = 0
    
    while True:
        line = f.readline()
        if line.strip()=="" :
            break
        fields = line.split(' ')
        if isTest == False:
            label = int(fields[0])
            y.append(label)
     
        cur_x = []
        for i in xrange(index,len(fields)):
            idx = d.get(fields[i])
            if idx == None:
                cur_x.append(len(d))
                d[fields[i]] = len(d)
            else:
                cur_x.append(idx)
        cur_str_x = [str(x) for x in cur_x]
        if isTest == True:
            print >> fm_test,str(y[cnt])+" "+" ".join(cur_str_x)
        else:
            print >> fm_train,str(y[cnt])+" "+" ".join(cur_str_x)
        cnt = cnt + 1
        if cnt % 1000000 == 0:
            print cnt

starttime = datetime.now()

d = {}

fm_train = open("after_index1","w")
#fm_test = open("../fm_test_1","w")

load_name_sample('../tmp/avazu_ad_user_v2',False)
#load_name_sample('../test_pre',True)

fm_train.close()
#fm_test.close()

#learner = field_fm(k,l,t,alpha,beta,max_feature,field_cnt)
endtime = datetime.now()
print (endtime-starttime).seconds
