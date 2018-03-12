#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import os,sys,re

def _now(format="%Y-%m-%d %H:%M:%S"):
	return datetime.datetime.now().strftime(format)

##### 可在脚本开始运行时调用，打印当时的时间戳及PID。
def job_start():
	print "[%s][PID:%s] job_start" % (_now(), os.getpid())

##### 可在脚本执行成功的逻辑分支处调用，打印当时的时间戳及PID。 
def job_success(msg):
	print "[%s][PID:%s] job_success:[%s]" % (_now(), os.getpid(), msg)
	sys.exit(0)

##### 可在脚本执行失败的逻辑分支处调用，打印当时的时间戳及PID。
def job_fail(msg):
	print "[%s][PID:%s] job_fail:[%s]" % (_now(), os.getpid(), msg)
	sys.exit(1)


def initialize_copyfile(verdir, bfverdir, projectpath, configpath):
	copy_config = [
	#'jsifs.ini',
	'app.properties',
	'jdbc.properties',
	'logback.xml'
	]
	bashprofile = '/home/jht/.bash_profile'
	with open(bashprofile) as f:
		data = f.read()
	#bfverdir = re.search(r'v_pjct=(.+)' , data).group(1)
	#configpath = 'WEB-INF/classes/config'
	os.chdir(projectpath)
	if not os.path.exists(bfverdir):
		job_fail('上一个版本目录不存在: '+bfverdir)
	for conf in copy_config:
		if not os.path.exists(bfverdir+'/'+configpath+'/'+conf):
			print os.getcwd()
			print bfverdir+'/'+conf
			job_fail('配置文件不存在: '+conf)
	if os.path.exists(verdir):
		job_fail('目录已存在: '+verdir)

	backupconfpath = verdir+'/beforeconf_'+bfverdir
	os.makedirs(backupconfpath)
	os.system("cp -f "+bfverdir+"/jsifs.ini "+backupconfpath)
	for conf in copy_config:
		os.system("cp "+bfverdir+"/"+configpath+"/"+conf+" "+backupconfpath)
	print ('修改v_pjct名字为:'+verdir)
	os.system('sed -i "s/^v_jsifs\s*=\s*.*/v_jsifs='+verdir+'/g" /home/jht/.bash_profile')


if __name__ == '__main__':

	job_start()
	verdir = sys.argv[1]
	bfverdir = sys.argv[2]
	projectpath = sys.argv[3]
	configpath = sys.argv[4]
	initialize_copyfile(verdir, bfverdir, projectpath, configpath)
###### 可在此处开始编写您的脚本逻辑代码
###### iJobs中执行脚本成功和失败的标准只取决于脚本最后一条执行语句的返回值
###### 如果返回值为0，则认为此脚本执行成功，如果非0，则认为脚本执行失败