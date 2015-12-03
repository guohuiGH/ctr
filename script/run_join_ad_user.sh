#########################################################################
# File Name: run_join_ad_user.sh
# Author:stone 
# mail: 
# Created Time: 2015年11月19日 星期四 12时36分55秒
#########################################################################
#!/bin/bash
python delete_repeat.sh
python join_ad_user_before.py
python generate_gbdt_input.py

