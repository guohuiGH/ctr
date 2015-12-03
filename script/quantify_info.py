# Author: guohui
ad_dic = dict()
user_dic = dict()
NONE_VALUE = "-1"

def parse_installs(installs):

	ranges = installs.strip(" ").split("-")
	#print ranges[0]

	left = int("".join((ranges[0].split(","))))

	#right = int(ranges[1].strip(","))
	if left < 100:
		return 1
	elif left < 1000:
		return 2
	elif left < 10000:
		return 3
	elif left < 100000:
		return 4
	elif left < 1000000:
		return 5
	elif left < 5000000:
		return 6
	elif left < 10000000:
		return 7
	elif left < 50000000:
		return 8
	elif left < 100000000:
		return 9
	else:
		return 10
	pass
	
def parse_size(ss):
	l = len(ss)
	ss = ss.upper()
	size = 0.0
	if ss.find("K") != -1:
		size = float(ss[0:l-1])/1000
		return size
	elif ss.find("GB") != -1:
		size = float(ss[0:l-2])*1000
		return size
	elif ss.find("G") != -1:
		size = float(ss[0:l-1])*1000
        else:
                size = float(ss)
	return float(size)


def quantifyAdInfo(file_name, file_name_2, file_name_3):
	global NONE_VALUE
	temp_file = open(file_name, "r")
        #temp_file2 = open(file_name_2, "r")
	ad_file = open(file_name_3, "w+")
	lines = temp_file.readlines()
        #temp_lines = temp_file2.readlines()
        #lines.extend(temp_lines)

	country_dic = dict()
	title_dic = dict()
	categry_dict = dict()

	count_ad = 0
	count_country = 0
	count_title = 0
	count_category = 0

	for line in lines:
		line_list = line.strip().split("@@")

		temp_line = ""
		
		ad_id = line_list[0]
		if ad_id not in ad_dic:
			ad_dic[ad_id] = count_ad
			count_ad += 1
		temp_line += str(ad_dic[ad_id]) + "@"

		country = line_list[1]
		if country not in country_dic:
			country_dic[country] = count_country
			count_country += 1;
		temp_line += str(country_dic[country]) + "@"

		platform = line_list[2]
		if platform == '101':
			temp_line += str("0@")
		else:
			temp_line += str("1@")

		title = line_list[3]
		if title not in title_dic:
			title_dic[title] = count_title
			count_title += 1
		temp_line += str(title_dic[title]) + "@"

		categry = line_list[4]
		if categry not in categry_dict:
			categry_dict[categry] = count_category
			count_category += 1;
		temp_line += str(categry_dict[categry]) + "@"


		if len(line_list[5]) > 2:
			#level = parse_installs(line_list[5])
			level = line_list[5]
			temp_line += (str(level) + "@")
		else:
			temp_line += (NONE_VALUE + "@")
			pass


		if len(line_list[6]) > 0:
			star = float(line_list[6])
			if star > 0.0:
				temp_line += (str(star) + "@")
			else:
				temp_line += (NONE_VALUE + "@")
		else:
			temp_line += (NONE_VALUE + "@")

		if len(line_list[7]) > 0:
			view_nums = int(line_list[7])
			if view_nums > 0:
				temp_line += (str(view_nums) )
			else:
				temp_line += (NONE_VALUE )
		else:
			temp_line += (NONE_VALUE)
		temp_line +=  "@"


		if len(line_list[8]) > 0:
	
			if line_list[8] == 'Varies with device':
				temp_line += (NONE_VALUE)
			else:
				size = parse_size(line_list[8])

				if size > 0.0:
					temp_line += (str(size))
				else:
					temp_line += (NONE_VALUE )
		else:
			temp_line += (NONE_VALUE)

		temp_line += "\n"

		ad_file.write(temp_line)
		#line = temp_file.readline()
		pass

	temp_file.close()
        #temp_file2.close()
	ad_file.close()
	pass


def quantifyUserInfo(file_name, file_name_2):
	temp_file = open(file_name, "r")
	user_file = open(file_name_2, "w+")

	line = temp_file.readline()
	#count_click = 0; count_total = 0
	count_user = 0
	count = 0
	count_invalid = 0

	while line:

		line_list = line.strip().split("@@")

		count +=1
		ad_id = line_list[0]
		if ad_id not in ad_dic:

			line = temp_file.readline()
			continue
		
		temp_line = ""
		temp_line += str(ad_dic[ad_id]) + ","

		user_id = line_list[1]
		if user_id == "Imei-xmodlite" or user_id == "Imei-xmodgame" or user_id == "":
			count_invalid += 1
			line = temp_file.readline()
			continue
		if user_id not in user_dic:
			user_dic[user_id] = count_user;
			count_user += 1
		temp_line += (str(user_dic[user_id]) + ",")
		try:
			click_value = line_list[2]
		except:
			click_value = '2105'
			print line
		if click_value < '2104':
			#count_click += 1
			temp_line += "1"
		else:
			temp_line += "0"
		#count_total += 1
		temp_line += "\n"

		user_file.write(temp_line)
		line = temp_file.readline()
		pass
	pass
	#print float(count_click)/(count_total)
	temp_file.close()
	user_file.close()
	print count
	print count_invalid

def mapUserAd(file_name, file_name_2):
	user_file = open(file_name, "w+")
	ad_file = open(file_name_2, "w+")
	for user in user_dic:
		user_file.write(user + "," + str(user_dic[user]) + "\n")
	for ad in ad_dic:
		ad_file.write(ad + "," + str(ad_dic[ad]) + "\n")
	user_file.close()
	ad_file.close()


if __name__ == '__main__':
	
	avazu_ad_file_name = "../tmp/avazu_ad_info"
	avazu_ad_quantify_file_name = "../tmp/avazu_ad_quantify"
        avazu_test_ad = "../tmp/test_avazu_ad_info"
	quantifyAdInfo(avazu_ad_file_name, avazu_test_ad, avazu_ad_quantify_file_name)
	avazu_user_file_name = "../tmp/avazu_user_info"
	avazu_user_quantify_file_name = "../tmp/avazu_user_quantify"
	quantifyUserInfo(avazu_user_file_name, avazu_user_quantify_file_name)
	avazu_map_user_file_name = "../tmp/avazu_map_user"
	avazu_map_ad_file_name = "../tmp/avazu_map_ad"
	mapUserAd(avazu_map_user_file_name, avazu_map_ad_file_name)

