#!/usr/bin/python
#cmd_sub.py
# -*- coding: utf-8 -*-
 
import subprocess
import os
import xlsxwriter
import signal

class Alarm(Exception):
    pass

def alarm_handler(signum,frame):
    raise Alarm
 
def execute(cmd,case) :
    print("case "+case)
    try:
       
        fd = subprocess.Popen(cmd, shell=True,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

        signal.signal(signal.SIGALRM,alarm_handler)
        signal.alarm(5) # 2sec.
        output=fd.communicate(case.encode())[0].decode()
        
        signal.alarm(0) # time reset.
        if(output=="hello world\n" or output=="hello world " or output=="hello world"):
            print("chk!")
        else: 
            output=output.split(' ')
        return fd.stderr,output
    except Alarm:
        print("long time")
        return -1,-1

def compile(cmd):
    fd = subprocess.Popen(cmd, shell=True,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    fd.communicate()
    return fd.stdout,fd.stderr

path="/home/kitoha/structure_homework/hw6/t"
folder="test"
k_path="rm "+"/home/kitoha/algorithm"+"/test"
count=2

for root,dirs,files in os.walk(path):
    rootpath =os.path.join(os.path.abspath(path),root)
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A'+str(1),"class number")
    worksheet.write('B'+str(1),"count")
    for file in files:
        try:
            IsTrue=False
            sum=0
            print(file)
            filepath = os.path.join(rootpath,file)
            fname, ext=os.path.splitext(filepath)

            if(ext==".c"):
                cmd="gcc -std=c99 -o test "+path+"/"+file
            elif(ext==".cpp"):
                cmd="g++ -std=c++11 -o test "+path+"/"+file+" -lstdc++"
            else :
                print("Not File Name Extension")
                continue
            #elif(ext==".java"):
             #   cmd="javac "+path+"/test13.java"
           
            #if(ext==".java"):
             #   cmd2="java test13"
            #else:
            
            cmd2="./"+folder
            compile(cmd)
            print(cmd)

            f3=open("/home/kitoha/algorithm/input.txt","r")
            input_path="/home/kitoha/structure_homework/hw6/test_input"
            output_path="/home/kitoha/structure_homework/hw6/test_output"
           
            for str_arr in f3.readlines():
               
                str_arr=str_arr.rstrip('\n')
            
                input_arr=input_path+"/input"+str_arr+".txt"
                output_arr=output_path+"/output"+str_arr+".txt"
             
                f2=open(input_arr,"r")
                f=open(output_arr,"r")
                output_line=f.readlines()
                out_line=""

                for s in output_line:
                    print(s.rstrip('\n'))
                    out_line=out_line+s.rstrip('\n')

                result=out_line
                cnt=0
                
                input_line=""
                lines=f2.readlines()

                c=0
                for line in lines:
                    if(c>0):
                        input_line=input_line+line.rstrip('\n')+" "
                    else :
                        input_line=input_line+line.rstrip('\n')+" "
                    c=c+1
                        
               
                std_out, output = execute(cmd2,input_line)
                
                if(output==-1):
                    print("TimeOut")
                    continue
                if(output==-2):
                    st=""
                    for s in file:
                        if((s>='a'and s<='z') or (s>='0' and s<='9')):
                            st=st+s
                        else:
                            break
                    sum=-1
                    break

                if(output=="hello world\n" or output=="hello world " or output=="hello world"):
                    worksheet.write('A'+str(count),file)
                    worksheet.write('B'+str(count),10)
                    count=count+1
                    IsTrue=True
                    break

                out=[]
                li=""
                chh=0
                for line in output:
                    if(line=='\n' or line==' '): continue
                    if(line.encode()!=''):
                        k=line.encode()
                        chh+=1
                        if(chh==1):
                            li+=k
                        elif(chh==2):
                            li=li+" "+k
                            

                              
                li=li.rstrip('\n')
                print("result")
                print(result)
                
                if(result==li):
                    print("pass")
                    out=[]
                    sum+=10
                else:
                    print("none pass")
                f.close()
                f2.close()
            if(IsTrue==False):
                st=""
                for s in file:
                    if((s>='a'and s<='z') or (s>='0' and s<='9')):
                        st=st+s
                    else:
                        break
                worksheet.write('A'+str(count),st)
                worksheet.write('B'+str(count),sum)
                count=count+1
            compile(k_path)
        except RuntimeError:
            print("RunTime Error\n")
        except TypeError:
            print("Type Error\n")
        except ValueError:
            print("ValueError "+output)

      
        
    workbook.close()



