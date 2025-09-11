#coding:utf-8
##https://felixc.at/2010/07/srt-multiline-convert-python/
#字幕文件必须是utf-8
import re
import sys
if len(sys.argv)<2: sys.exit(0)
filename = sys.argv[1]

f=open(filename,'r', encoding="utf-8")
a=f.read()

aa=a.split('\n\n')
f.close()
k=[]

for a in aa:
    if len(a.split('\n'))<2:
        for m in a.split('\n'): k.append(m)
        continue
    time = "\n".join(a.split('\n')[:2])
    chi = [x for x in a.split('\n')[2:] if x != x.encode('unicode-escape')]
    eng = [x for x in a.split('\n')[2:] if x == x.encode('unicode-escape')]

    k.append(time)
    if len(chi)>0: k.append(" ".join(chi))
    if len(eng)>0: k.append(" ".join(eng))
    k.append('')

f=open(filename+"_fixed.srt","w", encoding="utf-8")
for m in k:
    f.write(m +"\n")
f.close()