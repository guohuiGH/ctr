#########################################################################
# File Name: run_logic_regression.sh
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Thu 12 Nov 2015 02:32:26 PM CST
#########################################################################
#!/bin/bash

python fix_default_value.py

python gbdt_feature.py

cd ../feature/gbdt/
./gbdt -d 3 -t 19 ../../tmp/aua_test ../../tmp/aua_train ../../tmp/test ../../tmp/train

cd ../../script
python append_gbdt.py

cd ../training/liblinear-multicore-2.1-2/
./train -s 0 ../../tmp/train
./predict -b 1 ../../tmp/test train.model ../../tmp/predict_result

cd ../../script
python log_loss.py ../tmp/test ../tmp/predict_result
python calculate_f1.py ../tmp/test ../tmp/predict_result
