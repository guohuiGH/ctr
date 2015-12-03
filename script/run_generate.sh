#########################################################################
# File Name: run_generate.sh
# Author:stone 
# mail: 
# Created Time: 2015年10月22日 星期四 11时47分40秒
#########################################################################
#!/bin/bash
python join_ad_user_before.py
python generate_gbdt_input.py
sh delete_negative.sh
python separate_train_and_predict_data.py
sh ../stone/kaggle-avazu/script/run_bak.sh
python join_original_gbdt.py
python to_liblinear.py
