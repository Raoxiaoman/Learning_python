#!/usr/bin/python3
# -*- coding=UTF-8 -*-
import os
import sys

def print_error(lines):
    for line in lines:
        print(line)
        


def for_check(path,fname):
    files = os.listdir(path)
    files.sort()
    for file in files:
        if os.path.isdir(path +"/"+file):
            if(file == "32320162204138"):
                continue
            for_check(path+"/"+file,fname)
        if os.path.isfile(path +"/"+file):
            name,ext = os.path.splitext(file)

            if name == fname and name == "read1":
                f = open(path +"/"+file)
                iter_f = iter(f)
                lines = []
                for line in iter_f:
                    lines.append(line.strip())
                if len(lines) < 2:
                    part1 = lines[0] !="1,1"  
                    grade = 0
                    if not part1:grade = grade+3
                    print(path+"-"+name)
                    print("grade:"+str(grade))
                    print(lines)
                    continue
                part1 = lines[0] !="1,1"  
                part2 = lines[1] !="5,6"
                error = part1 or part2
                if error:
                    grade = 0
                    if not part1:grade = grade+3
                    if not part2:grade = grade+3
                    print(path+"-"+name)
                    print("grade:"+str(grade))
                    print(lines)

            if name == fname and name == "read2":
                f = open(path +"/"+file)
                iter_f = iter(f)
                lines = []
                for line in iter_f:
                    lines.append(line.strip())
                if len(lines) < 2:
                    part1 = lines[0] !="1,1"  
                    grade = 0
                    if not part1:grade = grade+3
                    print(path+"-"+name)
                    print("grade:"+str(grade))
                    print(lines)
                    continue
                part1 = lines[0] !="1,1"  
                part2 = lines[1] !="1,2"
                error = part1 or part2
                if error:
                    grade = 0
                    if not part1:grade = grade+3
                    if not part2:grade = grade+3
                    print(path+"-"+name)
                    print("grade:"+str(grade))
                    print(lines)

            if name == fname and name == "error1":
                f = open(path +"/"+file,encoding="gb2312")
                iter_f = iter(f)
                lines = []
                for line in iter_f:
                    lines.append("".join(line.split()))
                if len(lines) < 1:
                    print(path+"-"+name)
                    continue
                # print(lines)
                part1 = ("intx,n,s=0;" not in lines)   
                part2 = ("while(n>0)" not in lines)    
                part3 = ("n--;" not in lines) and ("n=n-1;" not in lines) and ("n=(n-1);" not in lines) 

                error = part1 or part2 or part3
                if error:
                    print(path+"-"+name)
                    grade = 0
                    if not part1:grade = grade+2
                    if not part2:grade = grade+2
                    if not part3:grade = grade+2
                    print(part1)
                    print(part2)
                    print(part3)
                    print("grade:"+str(grade))
                    # print_error1(lines)
            if name == fname and name == "error2":
                f = open(path +"/"+file,encoding="gb2312")
                iter_f = iter(f)
                lines = []
                for line in iter_f:
                    lines.append("".join(line.split()))
                if len(lines) < 1:
                    print(path+"-"+name)
                    continue
                # print(lines)
                part1 = ("charisu(charx)" not in lines)   
                part2 = ("{if(x<='Z'&&x>='A')return1;" not in lines)    
                part3 = ("while(y!='\\n')" not in lines) 
                part4 = ("if(isu(y)==1)n++;" not in lines) 
                part5 = ("y=getchar();" not in lines) 

                error = part1 or part2 or part3 or part4
                if error:
                    print(path+"-"+name)
                    grade = 0
                    if not part1:grade = grade+1
                    if not part2:grade = grade+1
                    if not part3:grade = grade+1
                    if not part4:grade = grade+2
                    if not part5:grade = grade+1
                    # print(part1)
                    # print(part2)
                    # print(part3)
                    # print(part4)
                    # print(part5)
                    print("grade:"+str(grade))
                    # print_error(lines)


    return

print(sys.argv)
print(len(sys.argv))
if len(sys.argv) > 2:
    for_check(sys.argv[1],sys.argv[2])
else:
    print("example:python3 for_check dir(目录名) read1(文件名不需要后缀)")
