 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import socket

#### introduction #############################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = 'GET / HTTP/1.1\nHost: '+server+'\n\n'

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096) #buffer size
# print(result)

while (len(result)>0):
	print(result)
	result=s.recv(1024)
###############################################################

##### simple port scanner ######################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def pscan(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False

for x in range(1,26):
	if pscan(x):
		print("Port", x, "is open!")
	else:
		print("Port",x,"is closed")
###############################################################

##### Threaded port scanner ###################################
import threading
from Queue import Queue

print_lock = threading.Lock()

server = 'pythonprogramming.net'

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((server,port))
		with print_lock:
			print('port',port,'is open!')
		con.close()
	except:
		pass

# The threader thread pulls an worker from the queue and processes it
def threader():
	while  True:
		worker = q.get()
		portscan(worker)
		q.task_done()
		print('one port scaned')

# Create the queue and threader 
q = Queue()

# 30 threads
for x in range(30):
	t=threading.Thread(target=threader)
	t.daemon = True
	t.start()

# check 100 ports
for worker in range(1,101):
	q.put(worker)

q.join()
###############################################################


##### sockets binding and listening ###########################
import sys
from thread import *
host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host,port))
except socket.error, e:
	print(str(e))

s.listen(6)  #kind of queue
print('Waiting for a connection')

def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))#in python2 no need to encode and decode

	while True:
		data = conn.recv(2048)
		reply = 'Server output: '+ data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode(reply))
	conn.close()

while True:

	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))

	start_new_thread(threaded_client, (conn,))



