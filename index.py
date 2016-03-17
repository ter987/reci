import urllib.request
import urllib.parse
import re
import json
import datetime
import chardet
f = urllib.request.urlopen("http://www.cnblogs.com/jenry/archive/2010/05/27/1744861.html")
html = f.read().decode('utf-8')
print(chardet.info(f))
exit()
reg = re.compile('<a.*?>(.+)<\/a>',re.I)
matchs = reg.findall(html)
handle = open('dics.txt','r+')
pydis = handle.read()

hd = open('domain'+datetime.datetime.now().strftime('%Y-%m-%d')+'.txt','w+')
#matchs = ['所首有词汇一页浏览', '网络词汇大全']
suffix = ['.com','.cn','.net']
for i in matchs:
    strs = ''
    t = 0
    if len(i)<10:
        while(t<len(i)):
            pos = pydis.find(i[t])
            if ord(i[t])>200 and pos != -1:
                b = 1
                while(pydis[pos+b] != ','):
                    strs = strs + pydis[pos+b:pos+b+1]
                    b +=1

            else:
                strs = strs + i[t]
            t += 1
        #str = str + '  '+
        if len(strs)<10:
            l = 0
            for a in suffix:
                url = 'http://checkdomain.xinnet.com/domainCheck?callbackparam=jQuery17203308473502664542_1458194172038&searchRandom=8&prefix='+strs+'&suffix='+a+'&_=1458194245054'
                f = urllib.request.urlopen(url)
                jsonh = f.read().decode('utf-8')
                regg = re.compile('\(\[(.+)\]\)',re.I)
                jsonh = regg.findall(jsonh)
                
                jsonh = json.loads(jsonh[0])
                print(jsonh)
                #exit()
                if len(jsonh['result'][0]['yes'])>0:
                       line = i+"\t"+strs+a+"\t"+str(jsonh['result'][0]['yes'][0]['price'])+"\n"
                       #print(line)
                       #exit()
                       hd.writelines(line)
                #print(len(jsonh['result'][0]['yes']))
                #exit()
                l += 1
#print(str)
print('OK')
