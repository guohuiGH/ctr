import sys

def calculate_f1(test_name, predict_name):
    test_file = open(test_name)
    predict_file = open(predict_name)
    test_line = test_file.readline()
    predict_line = predict_file.readline()
    predict_line = predict_file.readline()
    tp = 0; fp = 0; tn = 0; fn = 0
    while (test_line):
        test_value = int(test_line.strip().split(' ')[0])
        try:
            predict_value = int(predict_line.strip().split(' ')[0])
        except:
            predict_value = '1'
            print predict_line
        if test_value == predict_value:
            if test_value == 1:
                tp += 1
            else:
                fn += 1
        else:
            if test_value == 1:
                fp +=1
            else:
                tn +=1;
        test_line = test_file.readline()
        predict_line = predict_file.readline()
    print "tp: ", tp
    print "fn: ", fn
    print "fp: ", fp
    print "tn: ", tn
    if tp == 0:
        return 0
    p = float(tp)/float(tp+tn)
    r = float(tp)/float(tp+fp)
    f1 = 2*p*r/(p+r)
    test_file.close()
    predict_file.close()
    return f1



if __name__ == "__main__":
    test_name = sys.argv[1]
    predict_name = sys.argv[2]
    f1 = calculate_f1(test_name, predict_name)
    print "f1 value: " + str(f1)
