import os
import commands

jar = "/home/xueling/researchProjects/soot-infoflow-cmd-jar-with-dependencies.jar"
apk_orgPath = "/home/xueling/researchProjects/sourceDetection/apk_org/"

analysis_default = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-default/"
analysis_newSources = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-newSource/"
platformPath = "/home/xueling/researchProjects/platforms/"
SourceAndSinks_default = "/home/xueling/researchProjects/sourceDetection/SourceAndSinks_default.txt"


signaturePath = "/home/xueling/researchProjects/sourceDetection/sourceSignature/"

SourceAndSinks_newSources = "/home/xueling/researchProjects/sourceDetection/SourceAndSinks_newSources.txt"


def analyze(apk, str):


    if str == 'default':
        print 'Taint analysis with default SourceAndSinks...........'
        cmd_taint_default = 'java -jar ' + jar + ' -a ' + apk_orgPath + apk + '.apk -p' + platformPath + ' -s ' + SourceAndSinks_default + ' > ' + analysis_default + apk + ' 2>&1'
        print cmd_taint_default
        os.system(cmd_taint_default)

        grep_old = 'grep -i found ' + analysis_default + apk
        print grep_old
        print "Taint analysis resutl default source:"
        print commands.getoutput(grep_old)

    elif str == 'newSources':
        print 'Taint analysis with default SourceAndSinks + new Sources...........'

        newSources = open(signaturePath + apk).readlines()
        print newSources
        cmd = 'cp ' + SourceAndSinks_default + ' ' + SourceAndSinks_newSources
        print cmd
        os.system(cmd)

        fw = open(SourceAndSinks_newSources, 'a+')
        fw.write("% newSources" + '\n')
        fw.writelines(newSources)
        fw.close()

        cmd_taint_newSource = 'java -jar ' + jar + ' -a ' + apk_orgPath + apk + '.apk -p' + platformPath + ' -s ' + SourceAndSinks_newSources + ' > ' + analysis_newSources + apk + ' 2>&1'
        print cmd_taint_newSource
        os.system(cmd_taint_newSource)

        cmd = 'rm ' + SourceAndSinks_newSources
        print cmd
        os.system(cmd)

        print "Taint analysis resutl with new source: \n"
        grep_new = 'grep -i found ' + analysis_newSources + apk
        print grep_new
        print commands.getoutput(grep_new)




