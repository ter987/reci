# -*- coding:utf-8 -*-  
import requests
import re
import json
import datetime
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# test = 'abc你a好的是 阿斯蒂芬'
# test2 = '苏教阿骚了是你reer啊发'
# print(ord(test[6]))
# pos = test2.find(test[3:6])
# print(pos)
# print(test2[pos+3:pos+4])
# exit()



html = requests.get('http://blog.itpub.net/29625597/viewspace-1148243/')

source = html.content
#print(type(html.content))
reg = re.compile('<a.*?>(.+)<\/a>',re.I)
matchs = reg.findall(source)
handle = open('dics.dat','r+')
pydis = handle.read()
#print(type(pydis))
#print(matchs)
hd = open('domain'+datetime.datetime.now().strftime('%Y-%m-%d')+'.txt','w+')

suffix = ['.com','.cn','.net']
for i in matchs:
    strs = ''
    t = 0
    if len(i)<10:
        while(t<len(i)):
            #print(i)
            #exit()
            #pos = pydis.find(str(i[t]))
            
            if ord(i[t])>200:
                pos = pydis.find(str(i[t:t+3]))
                #print(i[t:t+3])
                #exit()
                b = 0
                while(pydis[pos+3+b] != ','):
                    #print(pydis[pos+b+3:pos+b+4])
                    #exit()
                    strs = strs + pydis[pos+b+3:pos+b+4]
                    b +=1
                    #print(pydis[pos+b:pos+b+1])
                    #exit()
            else:
                strs = strs + i[t]
            print(strs)
            #exit()
            t += 1
        #str = str + '  '+
        #print(strs)
        #exit()
        if len(strs)<10:
            
            l = 0
            for a in suffix:
                #print(strs)
                #exit()
                url = 'http://checkdomain.xinnet.com/domainCheck?callbackparam=jQuery17203308473502664542_1458194172038&searchRandom=8&prefix='+strs+'&suffix='+a+'&_=1458194245054'
                print(url)
                #exit()
                f = requests.get(url)
                #print(f.text)
                #exit()
                jsonh = f.content
                regg = re.compile('\(\[(.+)\]\)',re.I)
                jsonh = regg.findall(jsonh)
                
                jsonh = json.loads(jsonh[0])
                #print(jsonh)
                #exit()

                if len(str(jsonh['result'][0]['yes']))>0:
                       line = i+"\t"+strs+str(a)+"\t"+"\n"
                       print(line)
                       #exit()
                       hd.writelines(line)
                #print(len(jsonh['result'][0]['yes']))
                #exit()
                l += 1
#print(str)
print('OK')
