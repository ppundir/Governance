import urllib
import BeautifulSoup
state_counter = 0
from forum.models import State, Constituency
print "state data access"
constDict= {}
while 1:
	try:
		state_counter = int(state_counter)
		state_counter += 1
		if state_counter < 10:
			state_counter  =  '0' + str(state_counter)
		else:
			state_counter  =   str(state_counter)
		state_url = 'http://eciresults.nic.in/statewiseS' + state_counter + '.htm?st=S'+ state_counter
		a = urllib.urlopen(state_url)
		print state_url
		
		if a.code == 200:
			b=  a.read()
			###########################################
			soup = BeautifulSoup.BeautifulSoup(b)
			t = soup.findAll('tr')
			ff = t[3].findAll('tr')
			gg = ff[5].findAll('tr')
			ss  = gg[2].findAll('tr')
			d = ss[0].find('h3').text
			state = d.split(' Result Status')[0]
			constDict[state]=[]
			counter = 4
			while 1:				
				try:
					data  = ss[counter].findAll('td')
					mydict = {'const_name':data[0].text,'const_number':data[1].text,'candidate':data[2].text,'party':data[3].text}		
					counter +=1
					constDict[state].append(mydict)
				except Exception,e:
					break
			###########################################
		else:
			print "error in access of url " + state_url
					
		a.close()
	except Exception,e:
		print e
		break
	finally:
		a.close()

print "UT data access"
ut_counter = 0
while 1:
	try:
		ut_counter = int(ut_counter)
		ut_counter += 1
		if ut_counter < 10:
			ut_counter  =  '0' + str(ut_counter)
		else:
			ut_counter  =   str(ut_counter)
		union_url = 'http://eciresults.nic.in/statewiseU' + ut_counter + '.htm?st=U' + ut_counter
		print union_url
		########
		#######
		a = urllib.urlopen(union_url)
		if a.code == 200:
			b = a.read()
			###########################################
			soup = BeautifulSoup.BeautifulSoup(b)
			t = soup.findAll('tr')
			ff = t[3].findAll('tr')
			gg = ff[5].findAll('tr')
			ss  = gg[2].findAll('tr')
			d = ss[0].find('h3').text
			ut = d.split(' Result Status')[0]
			constDict[ut]=[]
			counter = 4			
			while 1:
				try:
					data  = ss[counter].findAll('td')			
					vdict = {'const_name':data[0].text,'const_number':data[1].text,'candidate':data[2].text,'party':data[3].text}
					counter +=1
					constDict[ut].append(vdict)
				except Exception,e:
					break
			###########################################
		else:
			print "error in access of url " + union_url
		
		a.close()
	except Exception,e:
		print e
		break
	finally:
		a.close()

print "access done"
for key,val in constDict.iteritems():
	p = State(name= key) 
	p.save()
	#val is a list of dictionaries
	for elem in val:
		p.constituency_set.create(name = elem.get('const_name') ,number = elem.get('const_number'),candidate= elem.get('candidate') ,party= elem.get('party'))
print "okokokkko"


