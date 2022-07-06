import socket
def server(): 

    sock = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
    port = 63905
    sock.connect(('192.168.2.61'),port)
    msg = sock.revc(1024)
    msg_decoded =msg.decode('utf-8')
    print("Message from server:"+ msg_decoded)
    msg_back=input("Do you want to Respond to the server? ")
    msg_back_encode=msg_back.encode("utf-8")
    sock.send(msg_back_encoded)



def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.2.61',63905))
    port = 63905
    s.listen(5)
    clientsocket,clientaddress =s.accept()
    print(clientsocket)
    print("Got a connection from %s." % str(clientaddress))
    msg = imput("Enter Any message:")
    client_encoded=msg.encode("utf-8")
    client.socket.send(msg_encoded)
    clientsoket.recv(1024)
    message_back= clientsocket.recv(1024)
    message_back_decoded=message_back_.decode('utf-8')
    print("respond from the client:")