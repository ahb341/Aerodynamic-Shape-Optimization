
import subprocess as sp
import os
import shutil
import sys
import string
import time
from pathlib import Path

xfoilpath = Path("datasets/xfoil.exe")
print(xfoilpath.name)
print(xfoilpath.suffix)
print(xfoilpath.stem)

if not xfoilpath.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
print(str(xfoilpath))
ps = sp.Popen(str(xfoilpath),stdin=sp.PIPE,stderr=sp.PIPE,stdout=sp.PIPE)
ps._stdin_write

def Xfoil(name, Ncrit, Re ):
    def Cmd(cmd):
        ps.stdin.write(cmd+'\n')
    try:
        os.remove(name+'.log')
    except :
        pass
    #    print ("no such file")
    # run xfoil
    ps = sp.Popen(str(xfoilpath) ,stdin=sp.PIPE,stderr=sp.PIPE,stdout=sp.PIPE)
    ps.stderr.close()
    # command part
    Cmd('load '+name+'.dat')
    Cmd('OPER')
    Cmd('Vpar')
    Cmd('N '+str(Ncrit))
    Cmd(' ')
    Cmd('visc '+str(Re))
    Cmd('PACC')
    Cmd(name+'.log')  # output file
    Cmd(' ')          # no dump file
    Cmd('aseq 0.0 15.0 1.0')
    Cmd(' ')     # escape OPER
    Cmd('quit')  # exit
    #resp = ps.stdout.read()
    #print "resp:",resp   # console ouput for debug
    ps.stdout.close()
    ps.stdin.close()
    ps.wait()
    #while (ps.returncode() == None):
    #    time.sleep(1)
    #ps.kill()

def getLDmax(name):
    filename = name+".log"
    f = open(filename, 'r')
    flines = f.readlines()
    LDmax = 0
    for i in range(12,len(flines)):
        #print flines[i]
        words = string.split(flines[i]) 
        LD = float(words[1])/float(words[2])
        if(LD>LDmax):
            LDmax = LD
    return LDmax

#Xfoil('mh32',9,500000)