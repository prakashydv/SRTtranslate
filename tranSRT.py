import re
import json
import urllib
import time
from datetime import datetime


def isNotNum(x):
	if x>='0' and x<='9':
		return False
	return True

# filename:source_language:target_language
while True:
	data=raw_input().split(':')
	if(len(data)==3):
		source_language=data[1]
		target_language=data[2]
		break;
	elif(len(data)==2):
		source_language=data[1]
		target_language="en"
		break;
	else:
		print u'format--->\n<filename.srt>:<source_language>:<destination_language>\nconsult README file for more information'
try:
	flog=open('log','a')
	f=open(data[0],'r')
	fout=open(target_language+'_'+data[0],'wb')
	flog.write(u'\n Start Time: '+str(datetime.now())+u'\nfile:'+data[0]+u'\n[source language:'+data[1]+u']\n[destination language: '+data[2]+']')
	
except:
	flog.write('\nTranslation unsuccessful.\nFinish time '+str(datetime.now())+u'\n\n')
	print 'file not found!'
	exit()
i=0
for line in f:
	if len(line)>1 and isNotNum(line):
		line=line.encode('utf8')
		url='http://syslang.com?src='+source_language+'&dest='+target_language+'+&text='+line.replace(' ','+')+'&email=prakashydv@gmail.com&password=frengly13&outformat=json'
		response=urllib.urlopen(url).read()
		print '['+str(i)+'] Translating : '+line
		JSONres = json.loads(response)
		
		if(len(JSONres)>1):
			print JSONres["translation"].encode('utf8')	
			fout.write(JSONres["translation"].encode('utf8'))
		else:
			fout.write("Error Translating")
		i+=1
	else:
		fout.write(line)
	time.sleep(3)

flog.write('\nTranslation successful.\nFinish time : '+str(datetime.now())+u'\n\n')
flog.close()
fout.close()
f.close()
print("Translation Finished!")
