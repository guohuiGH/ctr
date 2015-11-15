#########################################################################
# File Name: run_logic_regression.sh
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Thu 12 Nov 2015 02:32:26 PM CST
#########################################################################
#!/bin/bash

# test data is validation
#python fix_default_value.py ../tmp/avazu_sample_user ../tmp/aua_feature
#python gbdt_feature.py

#test data is new data
python fix_default_value.py ../tmp/avazu_user_test_quantify ../tmp/test_aua_feature
python test_gbdt_feature.py

cd ../feature/gbdt/
./gbdt -d 3 -t 19 ../../tmp/aua_test ../../tmp/aua_train ../../tmp/test_gbdt_out ../../tmp/train_gbdt_out

cd ../../script
python append_gbdt.py

cd ../training/liblinear/
./train -s 0 ../../tmp/train
./predict -b 1 ../../tmp/test train.model ../../tmp/predict_result


cd ../../script
python log_loss.py ../tmp/test ../tmp/predict_result
python calculate_f1.py ../tmp/test ../tmp/predict_result


python append_gbdt_dense.py

cd ../training/liblinear/
./train -s 0 ../../tmp/train_dense
./predict -b 1 ../../tmp/test_dense train_dense.model ../../tmp/predict_result

cd ../../script
python log_loss.py ../tmp/test_dense ../tmp/predict_result
python calculate_f1.py ../tmp/test_dense ../tmp/predict_result
