import os

apk = "com.gotv.nflgamecenter.us.lite"

jar = "/home/xueling/researchProjects/soot-infoflow-cmd-jar-with-dependencies.jar"
apk_orgPath = "/home/xueling/researchProjects/sourceDetection/apk_org/"

analysis_default = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-default/"
analysis_newSources = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-newSource/"
platformPath = "/home/xueling/researchProjects/platforms/"
SourceAndSinks_default = "/home/xueling/researchProjects/sourceDetection/SourceAndSinks_default.txt"
SourceAndSinks_newSources = "/home/xueling/researchProjects/sourceDetection/SourceAndSinks_newSources.txt"


cmd_taint_default = 'java -jar ' + jar + ' -a ' + apk_orgPath + apk + '.apk -p' + platformPath + ' -s ' + SourceAndSinks_default + ' > ' + analysis_default + apk + ' 2>&1'
print cmd_taint_default
os.system(cmd_taint_default)


#
# cmd_taint_newSource = 'java -jar ' + jar + ' -a ' + apk_orgPath + apk + '.apk -p' + platformPath + ' -s ' + SourceAndSinks_newSources + ' > ' + analysis_newSources + apk + ' 2>&1'
# print cmd_taint_newSource
# os.system(cmd_taint_newSource)