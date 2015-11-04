#encoding:utf-8
#!/usr/bin/python
import MySQLdb
import datetime
import copy
import os
import base64
import XXDataReport_pb2

counter = 0
avazu_user_file = open("/home/ec2-user/fmg-sysu/ctr/tmp/avazu_user_infosss", "w+")
avazu_ad_file = open("/home/ec2-user/fmg-sysu/ctr/tmp/avazu_ad_info", "w+")
#appnext_file = open("appnext_info", "w+")
avazu_ads = dict()

def initiaAd():
	conn = MySQLdb.connect("localhost", "root", "", "train_data")
	cursor = conn.cursor()
	sql = "select * from avazuad_info" 
	cursor.execute(sql)
	results = cursor.fetchall()
	for item in results:
		s = ""
		for i in range(2,len(item)):
			s += "@@" + str(item[i])
		avazu_ads[str(item[0])] = s
		avazu_ad_file.write(str(item[0]) + "@@" + str(item[1]) + s + "\n")
	conn.close()
	avazu_ad_file.close()

def read_eventlog(n):
	file_names = open(n, "r")
	file_list = file_names.readlines()

	for name in file_list:
		myfile=open(name.strip(),"r+")
		for line in myfile:
			mess=str(line.strip())
			mess=base64.b64decode(mess)
			yield mess



if __name__ == '__main__':
	k = 0
	j = 0
	start = datetime.datetime.now()
	initiaAd()
	for mess in read_eventlog("/home/ec2-user/fmg-sysu/ctr/tmp/eventlog_name"):
		rps = XXDataReport_pb2.RequestDataReport()
		rps.ParseFromString(mess)
		user_id = rps.userInfo.uuid.encode('utf-8')
		event_list = rps.commonEvents
		for i in range(len(event_list)):
			event_key = int(event_list[i].eventKey) 
			event_value = event_list[i].eventValue
			if event_key >= 2100 and event_key <= 2107 and len(event_value) > 0:
				
				temp_value = event_value[0].encode('utf-8')
				try:
					avazu_user_file.write(temp_value + "@@" + user_id + "@@" + str(event_key)+ "\n")
				except:
					j = j+1 
				k+=1
				if k%10000==0:
					print k
				break
		
	#appnext_file.close()
	end = datetime.datetime.now()
	print end - start
	print j
	avazu_user_file.close()
	


