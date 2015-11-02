#coding=utf-8
import string

def read_ad_file():
    adfile=open("../tmp/avazu_ad_quantify")
    adlist=[]
    for line in adfile.readlines():
        adsamp=line.strip('\n').split('@')
        adlist.append(adsamp)
    adfile.close()
    return adlist


def write_ad_file(binary_list):
    binfile=open("../tmp/avazu_ad_binary","w")
    for line in binary_list:
        binfile.write(line)
        binfile.write('\n')
    binfile.close()


def counting_star(ad_list):
    stars=[line[6] for line in ad_list if line[6] != '-1']
    minstar=string.atof(min(stars))
    maxstar=string.atof(max(stars));
    intervals=20
    increment=(maxstar-minstar)/intervals
    for line in ad_list:
        if line[6]=='-1':
            line[6]=str(intervals+1)
        else:
            line[6]=str(int((string.atof(line[6])-minstar)/increment))


def counting_installs(ad_list):
    mappingtable={}
    installrange=list(set([line[5] for line in ad_list]))
    installrange.sort()
    for r in xrange(len(installrange)):
        mappingtable[installrange[r]] = str(r)
    for line in ad_list:
        line[5]=mappingtable[line[5]]


def counting_size(ad_list):
    kbinterval=4
    kbincrement=float(1)/kbinterval
    mbinterval=10
    mbincrement=float(1000-1)/mbinterval
    gbinterval=2
    gbincrement=float(1000000-1000)/gbinterval
    for line in ad_list:
        if line[8]=='-1':
            line[8]='0'
        elif float(line[8]) < 1:
            line[8]=str(int(float(line[8])/kbincrement)+1)
        elif float(line[8]) < 1000:
            line[8]=str(int((float(line[8])-1)/mbincrement)+5)
        else:
            line[8]=str(int((float(line[8])-1)/mbincrement)+15)


def delete_invalid(ad_list):
    deletelist=[0,1,2,3,4,7];
    for col in deletelist:
        maxcount=max(map(int, [line[col] for line in ad_list]))
        for row in xrange(len(ad_list)):
            if ad_list[row][col]=='-1':
                ad_list[row][col]=str(maxcount+1)


def get_fix_length(ad_list):
    fixlens=[]
    for col in xrange(9):
        maxcount=max(map(int, [line[col] for line in ad_list]))
        fixlength=len(bin(int(maxcount))[2:]);
        fixlens.append(fixlength)
    return fixlens


def count_to_binary(source_str):
    binarystr=bin(int(source_str))[2:].zfill(fixlength)
    return binarystr


def get_matrix(fix_lens, ad_list):
    binarymat=[]
    for line in ad_list:
        binarymat.append(''.join([bin(int(line[col]))[2:].zfill(fix_lens[col]) for col in xrange(len(fix_lens))]))
    return binarymat


def main():
    ad_list=read_ad_file()
    counting_star(ad_list)
    counting_installs(ad_list)
    counting_size(ad_list)
    fix_lens=get_fix_length(ad_list)
    binary_mat=get_matrix(fix_lens, ad_list)
    write_ad_file(binary_mat)

if  __name__=="__main__":
    main()
