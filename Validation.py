import commands
analysisResultPath = "/home/xueling/researchProjects/sourceDetection/tainAnalysis-newSource/"
# analysisResultPath = "/Users/xueling/Downloads/"

logPath = "/home/xueling/researchProjects/sourceDetection/log/"

# log = "/Users/xueling/Downloads/temp.dms"
temp = "/home/xueling/researchProjects/sourceDetection/temp"

PII = {'utsaresearch2018@gmail.com', '757601f43fe6cab0', 'uuuu888'}

methodPath = "/home/xueling/researchProjects/sourceDetection/methods/"



validLeaksPath = "/home/xueling/researchProjects/sourceDetection/validLeaks/"




class SourceLine():             #flag: 1-toString, 0-resourceMethod, 2-sinkMethod
    def __init__(self, line, signature, toStringflag):
        self.line = line
        self.signature = signature
        self.toStringflag = toStringflag

list_SourceLine = list()

def validation(apk):
            # get source
    method = methodPath + apk
    methods = list()
    for line in open(method).readlines():
        methods.append(line.strip())

    leaks_org = open(analysisResultPath + apk).readlines()

    source_set = set()
    linesOfToString = list()

    print "extract sink and sources from taint analysis............."
    for line in leaks_org:
        line = line.strip()
        # print line
        if "was called with values from the following sources" in line:         # line of sink
            class_line = SourceLine(line, 0, 0)
            sink = line.split("<")[1].split('>')[0]
            class_line.signature = sink
            class_line.flag = 2
            list_SourceLine.append(class_line)
            print "sink:  " + sink
            continue
        elif '<' in line and '- - ' in line:         # line of source
            class_line = SourceLine(line, 0, 0)
            source = line.split('<')[1].split('>')[0]
            print "source:   " + source
            sourceClass = source.split(':')[0]
            sourceMethod = source.split(':')[1].split(' ')[2].split('(')[0]
            # print 'sourceClass:   ' + sourceClass
            # print 'sourceMethod:  ' + sourceMethod
            signature = sourceClass + '.' + sourceMethod
            class_line.signature = signature
            if signature in source_set:           # source exists
                for item in list_SourceLine:             # iterate all the line, and get the flag
                    if item.signature == signature:
                        class_line.flag = item.flag

            else:                                 # new source
                source_set.add(signature)
                if checkToString(signature, apk, methods):              # check toString
                    class_line.flag = 1
                else:
                    class_line.flag = 0
            list_SourceLine.append(class_line)



    removeFromLeaks(list_SourceLine, apk)


# callSite checking
            # source_callSite = line.split('in method')[1].lstrip(' <').rstrip('>')
            # # print "source_callSite " + source_callSite


def checkToString(signatrue, apk, methods):   # check if there exists more than one invocation of this method with different value
    log = logPath + apk
    if signatrue in methods:         # make sure its the new source we found
        cmd = 'grep ' + signatrue + ' ' + log + ' -B 1 > ' + temp
        commands.getoutput(cmd)
        for line in open(temp).readlines():
            if 'java.lang.Exception' not in line:
                continue
            if any(x in line for x in PII):   #  value is PII
                # print "any works"
                continue
            else:               # value has non-PII
                # print signatrue + ':    True'
                print "checking toString()................." + signatrue + '........True'
                return True
        # print signatrue + ':    False'
        print "checking toString()................." + signatrue + '.........False'
        return False
    else:
        print "not new sources"



def removeFromLeaks(list_SourceLine, apk):   # remove the toString methods and count valid leaks
    print "remove the toString() sources................"
    fw = open(validLeaksPath + apk, 'w')
    for item in list_SourceLine:
        if item.flag == 1:
            continue
        else:
            fw.write(item.line + '\n')
    fw.close()

    lines = open(validLeaksPath + apk).readlines()
    # print len(lines)
    validLeakCount = 0
    for line in lines:
        # print line
        if "The sink" in line and "was called with values from the following sources" in line:
            continue
        else:
            validLeakCount += 1
    print "after remove toString methods, found " + str(validLeakCount) + " valid leaks."

#
# checkCallSite