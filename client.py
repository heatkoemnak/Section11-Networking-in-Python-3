import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#port = 63905
s.bind(('192.168.2.61',63905)
port = 63905
s.listen(5)
clientsocket,clientaddress =s.accept()
print(clientsocket)
print("Got a connection from server.")
msg = imput("Enter Any message:")
client_encoded=msg.encode("utf-8")
client.socket.send(msg_encoded)
clientsoket.recv(1024)
message_back= clientsocket.recv(1024)
message_back_decoded=message_back_.decode('utf-8')
print("respond from the client:")