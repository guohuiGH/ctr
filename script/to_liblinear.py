def change():
    lines = open("../tmp/avazu_ad_user_join_gbdt",'r').readlines()
    fptr = open("../tmp/avazu_ad_user_feature_num",'w')
    for line in lines:
        line = line.strip()
        inf = line.split(' ')
        length = len(inf)
        for i in xrange(1,length):
            inf[i] = str(i) + ":" + inf[i]

        fptr.write("{}\n".format(" ".join(inf)))

if __name__ == "__main__":
    change()
