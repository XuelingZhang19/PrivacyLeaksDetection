# import sys
import os
import Decode
import Instrument
import RebuildApk
import keyGeneration
import AsignKey
import DownLoad
import GUITest
import IdentifySourceMethods
import ConvToSig
import TaintAnalysis
import Validation
import Uninstall
import Clear
import commands

apkNamelist = open('/home/xueling/researchProjects/sourceDetection/temp').readlines()
apkExists = os.listdir('/home/xueling/researchProjects/sourceDetection/apk_org/')
analysis_default = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-default/"
analysis_newSources = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-newSource/"

#download app
# for apk in apkNamelist:
#     apk = apk.strip()
#     if apk + '.apk' in apkExists:
#         print apk + " Exists!!!!"
#     else:
#         DownLoad.downLoad(apk)

#remove duplicate apk
# for apk in apkNamelist:
#     count = apkNamelist.count(apk)
#     if count > 1:
#         print apk


# taintAnalysis_default
for apk in apkNamelist:
    apk = apk.strip()
    print apk
    # Decode.decode(apk)
    # Instrument.insertLog(apk)
    # RebuildApk.rebuild(apk)
    # keyGeneration.generate(apk)
    # AsignKey.assign(apk)
    # TaintAnalysis.analyze(apk, 'default')
    # IdentifySourceMethods.findMethod(apk)
    # ConvToSig.convert(apk)
    # TaintAnalysis.analyze(apk, 'newSources')
    grep_old = 'grep -i found ' + analysis_default + apk
    print "Taint analysis resutl default source:"
    print commands.getoutput(grep_old)

    print "Taint analysis resutl with new source:"
    grep_new = 'grep -i found ' + analysis_newSources + apk
    print commands.getoutput(grep_new)
    print "\n\n"


