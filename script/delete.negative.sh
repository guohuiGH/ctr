#########################################################################
# File Name: delele_negative.sh
# Author:stone 
# mail: 
# Created Time: 2015年11月04日 星期三 07时01分58秒
#########################################################################
#!/bin/bash
cut -d ' ' -f1-9,11 ../tmp/avazu_ad_user_gbdt_input > ../tmp/avazu_ad_user_gbdt_input_v1
egrep -v " -1" ../tmp/avazu_ad_user_gbdt_input_v1 > ../tmp/avazu_ad_user_input_final
