
import os
import pexpect
import sys

rebuildApkPath = "/home/xueling/researchProjects/sourceDetection/rebuildApk/"
decodeFilePath = "/home/xueling/researchProjects/sourceDetection/decodeFile/"
apkNameList = []

# i = 1
# for file in os.listdir(decodeFilePath):
#     print i
#     if os.path.isfile(os.path.join(decodeFilePath, file)):
#         continue
#
#     if file + '.apk' in os.listdir(rebuildApkPath):
#         print "Exists!!!!"
#
#     else:
#         # rebuild
#         cmd = "apktool b %s%s -o %s%s" % (decodeFilePath, file, rebuildApkPath, file+".apk")
#         print cmd
#         os.system(cmd)
#     i += 1

def rebuild(apk):
    print 'rebuild apk.............'
    exists = os.listdir(rebuildApkPath)
    if apk + '.apk' in os.listdir(rebuildApkPath):
        print "rebuild Exists!!!!"

    else:
        # rebuild
        cmd = "apktool b %s%s -o %s%s" % (decodeFilePath, apk, rebuildApkPath, apk+".apk")
        print cmd
        os.system(cmd)