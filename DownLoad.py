import os
path = '/home/xueling/researchProjects/sourceDetection/apk_org/'
def downLoad(apk):
    cmd = 'gplaycli --device-codename shamu -d ' + apk + ' -f ' + path
    print cmd
    os.system(cmd)