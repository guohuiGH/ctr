def read_gbdt():
    lines = open("../stone/kaggle-avazu/train_gbdt_out_v4",'r').readlines()
    gbdt = []
    for line in lines:
        inf = line.strip().split(' ')
        gbdt.append(inf[1:])
    return gbdt

def read_original():
    lines = open("../tmp/avazu_ad_user_train",'r').readlines()
    fptr = open("../tmp/avazu_ad_user_join_gbdt",'w')
    gbdt = read_gbdt()
    count = 0
    for line in lines:
        inf = line.strip().split(' ')
        inf.extend(gbdt[count])
        count += 1
        fptr.write("{}\n".format(" ".join(inf)))

if __name__ == "__main__":
    read_original()
