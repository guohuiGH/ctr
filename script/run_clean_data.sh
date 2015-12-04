#########################################################################
# File Name: run.sh
# Author: guohui
# mail: 
# Created Time: Sun 11 Oct 2015 03:52:05 AM UTC
#########################################################################
#!/bin/bash



st=20151117
en=20151117
flag=1
python connect_info.py $st $en $flag
python quantify_info.py $st $en $flag
python sample_avazu_user.py $flag
python delete_repeat.py $flag
#for test_data

