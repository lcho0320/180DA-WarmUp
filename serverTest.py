import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
port = 8080
serv.bind((host_ip, port))
#serv.bind(('192.168.1.86,port))

# Assigns a port for the server that listens to clients connecting to this port
#serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	#from_client = '192.168.1.86'
	from_client = ''
	print ('Got connection from', addr)
	while True:
		data = conn.recv(4096)
		if not data: break
		from_client = data
		print(from_client.decode('ascii'))
		conn.send('I am SERVER'.encode())
	conn.close()
	print('client disconnected')
