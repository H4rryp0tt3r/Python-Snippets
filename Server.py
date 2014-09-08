import socket
from thread import *
def Client_Connection(conn):
	conn.send("#################   Welcome to Simple Math Test #################\n")
	for i in range(1,101,1):
		conn.sendall("%d + %d ?\n"%(i,i*8))
		while 1:
			ans=conn.recv(1024)
			if(ans[0:-1].isdigit()):
				ans=int(ans[0:-1])
				break
			else:
				conn.send("Invalid Input..Please try Again!\n")
		if ans!=(i+i*8):
			conn.send("Wrong Answer.Connection Closed.")
			conn.close()
			exit()
		else:
			conn.send("Correct Answer.\n")
	conn.sendall("Congratulations! You Scored 100/100.")
	conn.close()
try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error,msg:
	print "[-] Failed to Create Socket. Error Code %s ,Error Message : %s"%(msg[0],msg[1])
	exit(1)
print "[+] Socket Created.."
HOST=""
PORT=8999
try:
	s.bind((HOST,PORT))
except socket.error,msg:
	print "[-] Bind Failed. Error Code: %s , Error Message : %s"%(msg[0],msg[1])
	exit()
s.listen(10)
print "[+] Listening for Incoming Connections."
while 1:
	conn,addr=s.accept()
	print "[+] Connected with %s:%s"%(addr[0],addr[1])
	start_new_thread(Client_Connection,(conn,))
s.close()
