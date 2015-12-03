#######################################################
# File Name: log_loss.py
# Author: guohui
# mail:
# Created Time: Thr 11 Nov 2015 16:54:34 UTC
######################################################
#!/bin/bash
#coding=utf-8

import scipy as sp
import sys
def llfun(pred, act):
    epsilon = 1e-15

    pred = sp.maximum(epsilon, pred)

    pred = sp.minimum(1-epsilon, pred)


    ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = sum(ll)
    ll = ll * -1.0/len(act)
    return ll

def readfile(test_file_name, predict_file_name):
    test_file = open(test_file_name)
    predict_file = open( predict_file_name)

    test_lines = test_file.readlines()
    act = list()
    for line in test_lines:
        i = line.strip().split(' ')[0]
        temp = tuple()
        if i == '1':
            temp = (1,0)
        else:
            temp = (0,1)
        act.append(temp)
    
    line = predict_file.readline() 
    line = predict_file.readline()
    pred = list()
    while line:
        po = float(line.strip().split(' ')[1])
        ne = float(line.strip().split(' ')[2])
        temp = tuple()
        temp = (po,ne)
        pred.append(temp)
        line = predict_file.readline()
    return pred, act




if __name__=='__main__':
    (pred, act) = readfile(sys.argv[1], sys.argv[2])
    print "log loss:" + str(llfun(pred, act))

