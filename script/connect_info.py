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
    myfile = open('../tmp/temp', 'a')
    myfile2 = open('../data/user/avazu_user_info_' + str(sys.argv[1]))
    line = myfile2.readline()
    while line:
        myfile.write(line)
        line = myfile2.readline()
    myfile.close()
    myfile2.close()

if __name__=='__main__':
    connect_file()
