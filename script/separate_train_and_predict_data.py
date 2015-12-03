#Author: zhang yan
import random

def select():
    lines = open("../tmp/avazu_ad_user_sample",'r').readlines()
    fptr1 = open("../tmp/avazu_ad_user_sample_train",'w')
    fptr2 = open("../tmp/avazu_ad_user_sample_predict",'w')
    for line in lines:
        line = line.strip()
        num = random.randint(1,10)
        if num == 5:
            fptr2.write("%s\n" %line)
        else:
            fptr1.write("%s\n" %line)

if __name__ == "__main__":
    select()

