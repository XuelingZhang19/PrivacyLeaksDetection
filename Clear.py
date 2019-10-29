import os
decodeFilePath = "/home/xueling/researchProjects/sourceDetection/decodeFile/"
rebuildApkPath = "/home/xueling/researchProjects/sourceDetection/rebuildApk/"
apk_signedPath = "/home/xueling/researchProjects/sourceDetection/apk_signed/"
logPath = "/home/xueling/researchProjects/sourceDetection/log/"
methodPath = "/home/xueling/researchProjects/sourceDetection/methods/"


def clear(apk):
    # cmd_1 = 'rm -r ' + decodeFilePath + apk
    # print cmd_1
    # os.system(cmd_1)
    cmd_2 = 'rm ' + rebuildApkPath + apk + '.apk'
    print cmd_2
    os.system(cmd_2)

    cmd_3 = 'rm ' + apk_signedPath + apk + '.apk'
    print cmd_3
    os.system(cmd_3)

    cmd_4 = 'rm ' + logPath + apk
    print cmd_4
    os.system(cmd_4)

    cmd_5 = 'rm ' + methodPath + apk
    print cmd_5
    os.system(cmd_5)


