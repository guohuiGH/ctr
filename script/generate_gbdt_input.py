#Author: stone
def counting_installs(ad_list):
    mappingtable = {}
    installrange = list(set([line[5] for line in ad_list]))
    installrange.sort()
    for r in xrange(len(installrange)):
        mappingtable[installrange[r]] = str(r)
    for line in ad_list:
        line[5] = mappingtable[line[5]]
        if line[10] == "0":
            line[10] = str(-1)

def read_file():
    lines = open("../tmp/avazu_ad_user_original",'r').readlines()
    ad_list = []
    for line in lines:
        ad = line.strip().split('@')
        ad_list.append(ad)

    counting_installs(ad_list)
    fptr = open("../tmp/avazu_ad_user_gbdt_input",'w')
    for line in ad_list:
        fptr.write("%s " %line[10])
        fptr.write("{}\n".format(" ".join(line[:10])))

if __name__ == "__main__":
    read_file()
