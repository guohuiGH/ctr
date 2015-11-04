#encoding:utf-8
#!/usr/bin/python
import MySQLdb
import datetime
import copy
import os
import base64
import XXADLog_pb2

avazu_count = dict()

def read_adlog(n):
	file_names = open(n, "r")
	file_list = file_names.readlines()

	for name in file_list:
		myfile=open(name.strip(),"r+")
		for line in myfile:
			mess=str(line.strip())
			mess=base64.b64decode(mess)
			yield mess


def inesrt_into_ad_avazuad_db(ad_id, country, platform, title, category,star,installed_num, view_num,app_size):
	conn = MySQLdb.connect("localhost", "root", "", "train_data")
	cursor = conn.cursor()
	sql = """create table if not exists avazuad_info(
			ad_id varchar(64) not null,
			country varchar(8) not null,
			platform varchar(8) not null,
			title varchar(512) not null,
			category varchar(256) not null,
			installs varchar(128) not null,
			star varchar(16) not null,
			view_num varchar(32) not null,
			app_size varchar(32) not null,
			primary key(ad_id)
		)"""
	cursor.execute(sql)
	#sql2 = "create index ad_id on xxad_info(ad_id)"
	#cursor.execute(sql2)
	sql3 = "insert ignore into avazuad_info(ad_id, country, platform, title, category, star, installs, view_num, app_size) values ('%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')" % (ad_id, country, platform, title, category,star,installed_num, view_num,app_size)
	cursor.execute(sql3)
	conn.commit()
	conn.close()


def insert_into_ad_appnextad_db(ad_id, country, platform, title, idx, category):
	conn = MySQLdb.connect("localhost", "root", "", "train_data")
	cursor = conn.cursor()
	sql = """create table if not exists appnextad_info(
			ad_id varchar(64) not null,
			country varchar(8) not null,
			platform varchar(8) not null,
			title varchar(512) not null,
			idx varchar(32) not null,
			category varchar(256) not null
		)"""
	cursor.execute(sql)
	#sql2 = "create index ad_id on xxad_info(ad_id)"
	#cursor.execute(sql2)
	sql3 = "insert into appnextad_info(ad_id, country, platform, title, idx, category) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (ad_id, country, platform, title, idx, category)
	cursor.execute(sql3)
	conn.commit()
	conn.close()

def parsesrc(ader, src):
	category="" 
	star=""
	installs="" 
	view_num="" 
	appsize=""
	if ader == "AvazuAd":
		src_list = src.split("\\\"")
		#print src_list
		for i in range(len(src_list)):
			if src_list[i] == "appcategory":
				i = i + 2
				category = src_list[i]
				continue
			if src_list[i] == "appinstalls":
				i = i + 2
				installs = src_list[i]
				continue
			if src_list[i] == "apprating":
				i = i + 2
				star = src_list[i]
				continue
			if src_list[i] == "appreviewnum":
				i = i + 2
				view_num = src_list[i]
				continue
			if src_list[i] == "appsize":
				i = i + 2
				app_size = src_list[i].split("M")[0]
				continue
		return category,star, installs, view_num, app_size
	if ader == "AppnextAd":
		src_list = src.split("\\\"")
		#print src_list
		for i in range(len(src_list)):
			if src_list[i] == "categories":
				i = i + 2
				category = src_list[i]
				continue
			if src_list[i] == "idx":
				i = i + 2
				idx = src_list[i]
				continue
		return category, idx

	pass

if __name__ == '__main__':
	k = 0
	count = 0
	for mess in read_adlog("/home/ec2-user/fmg-sysu/ctr/tmp/adlog_name"):
		rps = XXADLog_pb2.XXADAwsInfo()
		rps.ParseFromString(mess)
		ad_id = rps.ad_id.encode('utf-8')
		platform = str(rps.platform).encode('utf-8')
		country = rps.country_code.encode('utf-8')
		ader = rps.ader
		title = MySQLdb.escape_string(rps.title.encode('utf-8'))
		src = rps.src.encode('utf-8')
		if ader == "AvazuAd":
			(category,star,installed_num, view_num,appsize) = parsesrc(ader, src)
			inesrt_into_ad_avazuad_db(ad_id, country, platform, title, category,star,installed_num, view_num,appsize)
		#if ader == "AppnextAd":
			#category, idx = parsesrc(ader, src)
			#insert_into_ad_appnextad_db(ad_id, country, platform, title, idx, category)
			if ad_id not in avazu_count:
				avazu_count[ad_id] = count;
				count +=1;
			k+= 1
			if k % 100 == 0:
				print k


