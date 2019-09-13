
import pexpect
import sys
import os

keyPath = "/home/xueling/researchProjects/sourceDetection/keys/"
apk_signedPath = "/home/xueling/researchProjects/sourceDetection/apk_signed/"
rebuildApkPath = "/home/xueling/researchProjects/sourceDetection/rebuildApk/"
apkNameList = []


def assign(apk):
        # key = file[:-4] + ".keystore"
    if apk + '.apk' in os.listdir(apk_signedPath):
        print apk + ' exists !!!'
    else:
        key = apk + ".keystore"
        cmd = "jarsigner -verbose -keystore %s%s -storepass 123456 -signedjar %s%s %s%s abc.keystore" %(keyPath, key,apk_signedPath, apk + '.apk', rebuildApkPath, apk + '.apk')
        print cmd
        os.system(cmd)


