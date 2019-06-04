import socket
s=socket.socket()
print("socket created successfully")
port = 12345
s.bind(('',port))
print("socket binded to port %s"%(port))
s.listen(5)
print ("socket is listening...")
while True:
	c,addr=s.accept()
	print("got a connection from",addr)
	str="thank you for connecting"
	c.sendall(str.encode('utf-8'))
	c.close()
