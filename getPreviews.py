#!/usr/bin/python

import re
import urllib2, urllib
from bs4 import BeautifulSoup


##Connect to www.academiadasapostas.com
fileObj = open('previews_links',"w")
usock = urllib.urlopen("https://www.academiadasapostas.com/")
lines=usock.readlines()
usock.close()
line_count=0
games=[]

##Get Previews games links
for line in lines:
	line_count+=1
	#print line
	if "match_preview" in line:
		#check=lines[line_count-12]
		#print check
		print line
		#game=line.split('" >')[0]
		game=line.split('href="')[-1]
		game=game.split('">Previ')[0]
		print game
		fileObj.write(game+'\n')
fileObj.close()

##Get Previews info for each game
def xmlTable(url):
	response = urllib2.urlopen(url)
	html_ = response.read()
	html=re.sub('&nbsp;','_',html_)
	#print html
	soup = BeautifulSoup(html)
	teams = soup.title.text.encode('utf-8').strip()
	fileObj.write('===> '+teams+'\n'+'\n')
	print '===> '+teams+'\n'+'\n'
	previewsTxt = soup.find('div',{"class":"preview_intro"})
	#print previewsTxt
	previewsTxt = previewsTxt.text.encode('utf-8').strip()
	fileObj.write(previewsTxt)
	fileObj.write('\n'+'\n'+'#####################################################################################################################################################################################'+'\n')
	print previewsTxt
	print '\n'+'\n'+'#####################################################################################################################################################################################'+'\n'
	return

##Print to File
f = open('previews_links')
fileObj = open('previews_of_today.txt',"w")
for line in f:
	#print line
	xmlTable(line)
f.close()
fileObj.close()

