import sys

def calculate_f1(test_name, predict_name):
    test_file = open(test_name)
    predict_file = open(predict_name)
    test_line = test_file.readline()
    predict_line = predict_file.readline()
    predict_line = predict_file.readline()
    user_dic = dict()
    count = 0
    while (test_line):
        test_value = int(test_line.strip().split(' ')[0])
        user_id = test_line.strip().split(' ')[1]
        temp_list = [0,0,0,0]
        if user_id in user_dic.keys():
            temp_list = user_dic[user_id]
        else:
            user_dic[user_id] = temp_list

        try:
            predict_value = int(predict_line.strip().split(' ')[0])
        except:
            predict_value = '1'
            print predict_line
        #tp,fn,fp,tn
        if test_value == predict_value:
            if test_value == 1:
                temp_list[0] += 1
            else:
                temp_list[1] += 1
        else:
            if test_value == 1:
                temp_list[2] +=1
            else:
                temp_list[3] +=1
        count += 1
        #if count %1000==0:
        #    print count
        user_dic[user_id] = temp_list
        test_line = test_file.readline()
        predict_line = predict_file.readline()
    sum_p = list(); sum_r = list(); sum_f1 = list()
    print "done"
    for user_id in user_dic.keys():
        [tp,fn,fp,tn] = user_dic[user_id]
        if (tp==0 and tn==0) or (tp==0 and fp== 0):
            continue
        if tp == 0:
            continue
        p = float(tp)/float(tp+tn)
        r = float(tp)/float(tp+fp)
        f1 = 2*p*r/(p+r)
        sum_p.append(p); sum_r.append(r); sum_f1.append(f1)
    #print user_dic
    #print len(sum_p)
    print "p: " + str(sum(sum_p)/len(user_dic))
    print "r: " + str(sum(sum_r)/len(user_dic))

    test_file.close()
    predict_file.close()
    return sum(sum_f1)/len(user_dic)



if __name__ == "__main__":
    test_name = sys.argv[1]
    predict_name = sys.argv[2]
    f1 = calculate_f1(test_name, predict_name)
    print f1
