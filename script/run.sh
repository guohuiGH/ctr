#########################################################################
# File Name: run.sh
# Author: guohui
# mail: 
# Created Time: Sun 11 Oct 2015 03:52:05 AM UTC
#########################################################################
#!/bin/bash

t1=20151116
t2=20151116
cd /home/ec2-user/fmg-sysu/ctr/script/
#python get_file_name.py $t1 $t2

cd /home/ec2-user/fmg-sysu/adlog-demo/
#python read_ad_info.py 

cd /home/ec2-user/fmg-sysu/eventlog-demo/
#for train_data
#python read_event_info.py $t1

#connect user info
cd /home/ec2-user/fmg-sysu/ctr/script/
python connect_info.py $t2


#connect ad info
a='../data/ad/avazu_ad_info_'
b="${a}${t2}"
cp $b ../tmp/avazu_ad_info2
# for test_data
#python read_event_info.py 0

# for train data
#cd /home/ec2-user/fmg-sysu/ctr/script/
#python quantify_info.py
#cd /home/ec2-user/fmg-sysu/ctr/script/
#python sample_avazu_user.py
#python delete_repeat.py
#for test_data
#cd /home/ec2-user/fmg-sysu/ctr/script/
#python quantify_test_user.py
