import urllib2

import json
import sys

def get_marathon_config(addr,app):
    r = urllib2.urlopen(addr)
    return r.read()

if __name__ == '__main__':
    print("Run script.")
    if len(sys.argv)<3:
        print("Run with marathon url and group param: get_config_py3.py <url> <app>")
        exit()
    else:
        url = sys.argv[1]
        app = sys.argv[2]
        response = get_marathon_config(url,app)
        json_obj = json.loads(response)
        apps = json_obj['apps']
        theApp = [x for x in apps if x['id'] == app][0]
        tasks = theApp['tasks']
        hostAndPorts = [(x['host'],x['ports'][0]) for x in tasks]

        print('find nodes:',hostAndPorts)
        f = open("ssh_config",'w')
        hostFile = open("hostfile","w")
        f.write("StrictHostKeyChecking no\n")
        index = 1
        for node in hostAndPorts:
            nodeName = "node"+str(index)
            f.write("HOST "+nodeName+"\n")
            f.write("\t HostName "+node[0]+"\n")
            f.write("\t Port "+str(node[1])+"\n")
            f.write("\t User tutorial\n")
            hostFile.write(nodeName+" slots=1\n")
            index+=1
        f.close()
        hostFile.close()

