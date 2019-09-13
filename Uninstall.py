import os
import commands
APKpath = "/home/xueling/researchProjects/sourceDetection/apk_org/"

def uninstall(apk):
    packageName = getPackageName(APKpath + apk + '.apk')

    cmd_remove = "adb uninstall %s" % packageName
    print cmd_remove
    os.system(cmd_remove)


def getPackageName(installName):
    # installName = apk_signedPath + installName
    cmd = 'aapt dump badging "%s" '%installName
    print cmd
    str= os.popen(cmd).readlines()[0].split(" ")[1]
    return str[6:-1]