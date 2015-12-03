#########################################################################
# File Name: run.sh
# Author: guohui
# mail: 
# Created Time: Sun 11 Oct 2015 03:52:05 AM UTC
#########################################################################
#!/bin/bash





# for test_data
#python read_event_info.py 0

# for train data
cd /home/ec2-user/fmg-sysu/ctr/script/
python quantify_info.py
cd /home/ec2-user/fmg-sysu/ctr/script/
python sample_avazu_user.py

python delete_repeat.py
#for test_data
cd /home/ec2-user/fmg-sysu/ctr/script/
#python quantify_test_user.py 20151116
