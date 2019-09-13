import os

apk_signedPath = "/home/xueling/researchProjects/sourceDetection/apk_signed/"
apk_orgPath = "/home/xueling/researchProjects/sourceDetection/apk_org/"
#

def install(apk, str):
    if str == 'org':
        cmd_install = 'adb install ' + apk_orgPath + apk + '.apk'
        print cmd_install
        os.system(cmd_install)

    if str == 'new':
        cmd_install = 'adb install ' + apk_signedPath + apk + '.apk'
        print cmd_install
        os.system(cmd_install)
        cmd_logcat_c = 'adb logcat -c'
        print cmd_logcat_c
        os.system(cmd_logcat_c)
        logPath = '/home/xueling/researchProjects/sourceDetection/log/'
        cmd_logcat_out = 'adb logcat > ' + logPath + apk
        print cmd_logcat_out
        os.system(cmd_logcat_out)