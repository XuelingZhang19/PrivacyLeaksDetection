SourceAndSinks_default = "/home/xueling/researchProjects/sourceDetection/SourceAndSinks_default.txt"
signaturePath = "/home/xueling/researchProjects/sourceDetection/sourceSignature/"
apk = 'com.contextlogic.wish';

fw = open(signaturePath + apk + '_2', 'w')


newSource = open(signaturePath +apk).readlines();
defultSource = open(SourceAndSinks_default).readlines();
for source in newSource:
    if source in defultSource:
        print source + "exists.....";
    else:
        print source
        fw.writelines(source)

fw.close()

