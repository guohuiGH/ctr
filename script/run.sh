#########################################################################
# File Name: run.sh
# Author: guohui
# mail: 
# Created Time: Sun 11 Oct 2015 03:52:05 AM UTC
#########################################################################
#!/bin/bash


cd /home/ec2-user/fmg-sysu/ctr/script/
python get_file_name.py

cd /home/ec2-user/fmg-sysu/adlog-demo/
python read_ad_info.py

cd /home/ec2-user/fmg-sysu/eventlog-demo/
#for train_data
python read_event_info.py 1

# for test_data
#python read_event_info.py 0

# for train data
cd /home/ec2-user/fmg-sysu/ctr/script/
python quantify_info.py
cd /home/ec2-user/fmg-sysu/ctr/script/
python sample_avazu_user.py

#for test_data
cd /home/ec2-user/fmg-sysu/ctr/script/
#python quantify_test_user.py
