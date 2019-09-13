# this script pick the senstive methods which returns email address from ststem log
import os
import commands

# AdsID  ce3b1e33-8e03-4664-aafc-8d50f474a442
#device_serial	ZX1G22KHQK
IMEI = "355458061189396"
Serial = "ZX1G22KHQK"
Email = "utsaresearch2018@gmail.com"
AndroidID = "757601f43fe6cab0"
AndroidID_new = 'a54eccb914c21863'
PassWord = 'uuuu8888'

PII = (IMEI, Serial, Email, AndroidID, AndroidID_new, PassWord)

logPath = "/home/xueling/researchProjects/sourceDetection/log/"
methodPath = "/home/xueling/researchProjects/sourceDetection/methods/"


def findMethod(log):
    setMethods = set()     # remove the duplicated methods from log

    flag = 0

    fw = open(methodPath + log, 'a')

    lines = open(logPath + log).readlines()
    for line in lines:
        line = line.strip()
        if "W System.err: java.lang.Exception:" in line:
            if any(s in line for s in PII):
                print line
                flag = 1
                continue

        if flag == 1:
            if "W System.err: 	at" in line:
                # print line
                method = line.split("(")[0].split("W System.err: 	at ")[1]
                # print method
                setMethods.add(method)
                flag = 0
                continue
            else:
                print line
                print "the next line is not correct"


    for method in setMethods:
        fw.writelines(method + '\n')

files = os.listdir(methodPath)

def identify(apk):
    print 'Identify PII methods............'
    if apk in files:
        print apk + 'exists!!'
    else:
        findMethod(apk)