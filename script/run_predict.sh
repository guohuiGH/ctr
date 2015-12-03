#author:stone
#predict only

#python join_userfeature_auafeature.py
#python ../feature/one_hot_encoded_more.py
python ../feature/one_hot_encoded_less.py
python separate_train_and_predict_data_tmp.py

cd ../training/liblinear/
./train -s 0 ../../tmp/avazu_onehot_train
./predict -b 1 ../../tmp/avazu_onehot_predict avazu_onehot_train.model ../../tmp/predict_result

cd ../../script
python log_loss.py ../tmp/avazu_onehot_predict ../tmp/predict_result
python calculate_f1.py ../tmp/avazu_onehot_predict ../tmp/predict_result
