import urllib.request
import urllib.parse
import re
f = urllib.request.urlopen("http://wangci.net/futureWord.html")
html = f.read().decode('gbk')
reg = re.compile('<a.*?>(.+)?<\/a>',re.I)
matchs = reg.findall(html)
print(matchs)