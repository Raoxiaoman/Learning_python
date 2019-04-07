#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def mvn_run_java(method,ClassName):
    pwd = os.getcwd()
    print(pwd)
    while pwd != "/":
        files = os.listdir(pwd)
        for file in files:
            if os.path.isfile(pwd +"/"+file):
                if file == "pom.xml":
                    abs = pwd+"/"+file
                    print(abs)
                    if (method == "compile"):
                        p = subprocess.Popen('mvn -f '+abs+ ' compile', \
                                shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                    elif (method == "run"):
                        cmd = 'mvn -f '+abs+ ' exec:java -Dexec.mainClass="com.raohui.' + ClassName + '"'
                        print(cmd)
                        p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    elif (method == "deploy"):
                        p = subprocess.Popen('mvn -f '+abs+ ' clean package tomcat7:deploy', \
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    elif (method == "test"):
                        p = subprocess.Popen('mvn -f '+abs+ ' test', \
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    elif (method == "redeploy"):
                        p = subprocess.Popen('mvn -f '+abs+ ' clean package tomcat7:redeploy', \
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    for line in p.stdout.readlines():
                        print(line)
                    return
        ppwd = os.path.abspath(os.path.dirname(pwd))
        # print(ppwd)
        pwd = ppwd

# print(sys.argv)
# print(len(sys.argv))
if len(sys.argv) > 2:
    mvn_run_java(sys.argv[1],sys.argv[2])
else:
    print("example:python3 mvn_run_java.py compile/run/deploy/redeploy ClassName")
