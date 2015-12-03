#Author: zhang yan
import random

def select():
    lines = open("../tmp/avazu_ad_user_onehot",'r').readlines()
    fptr1 = open("../tmp/avazu_ad_user_sample",'w')
    for line in lines:
        line = line.strip()
        inf = line.split(' ')
        if inf[0] == '1':
            fptr1.write("%s\n" %line)
        else:
            num = random.randint(1,11)
            if num == 5:
                fptr1.write("%s\n" %line)

if __name__ == "__main__":
    select()

