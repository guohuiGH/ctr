#########################################################################
# File Name: connect_info.py
# Author: 
# mail: 
# Created Time: Wed 25 Nov 2015 08:21:04 AM UTC
#########################################################################
#!/bin/bash
#coding=utf-8

import sys

def connect_file():
    if sys.argv[3] == '1':
        myfile = open('../data/test/user_info_' + str(sys.argv[1]) + '_' + str(sys.argv[2]), 'w')
    else:
        
        myfile = open('../data/train/user_info_' + str(sys.argv[1]) + '_' + str(sys.argv[2]), 'w')
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        try:
            myfile2 = open('../data/user/avazu_user_info_' + str(i))
        except:
            print i
            continue
        line = myfile2.readline()
        while line:
            myfile.write(line)
            line = myfile2.readline()
        myfile2.close()
    myfile.close()

if __name__=='__main__':
    connect_file()
