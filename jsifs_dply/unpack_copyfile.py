#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import os
import sys

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


def unpack(projectpath , bfverdir , verdir , configpath):
	copy_config = [
	#'jsifs.ini',
	'app.properties',
	'jdbc.properties',
	'logback.xml'
	]
	os.chdir(projectpath+'/'+verdir)
	print (projectpath+'/'+verdir)
	print (os.getcwd())
	os.system("unzip -o *.zip")
	os.system("mv linux_64/* .")
	#os.system("jar xvf *.war")
	os.system("cp -f beforeconf_"+bfverdir+"/jsifs.ini .")
	for conf in copy_config:
		os.system("cp -f beforeconf_"+bfverdir+"/"+conf+" "+configpath)



if __name__ == '__main__':

	job_start()
	projectpath = sys.argv[1]
	verdir = sys.argv[2]
	bfverdir = sys.argv[3]
	configpath = sys.argv[4]
	unpack(projectpath , bfverdir , verdir , configpath)
	job_success('done')

###### 可在此处开始编写您的脚本逻辑代码
###### iJobs中执行脚本成功和失败的标准只取决于脚本最后一条执行语句的返回值
###### 如果返回值为0，则认为此脚本执行成功，如果非0，则认为脚本执行失败
