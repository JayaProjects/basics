# Line counting and Word counting:
import os,sys
fname = input("Enter file name =")
f = open(fname,'r')
ln=wd=cd=0
for line in f:
    ln = ln+1
    cd = cd+len(line)
    word = line.split()
    wd = wd + len(word)
print("No of lines =",ln)
print("No of words =",wd)
print("No of words =",cd)