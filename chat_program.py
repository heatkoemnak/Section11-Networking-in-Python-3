from datetime import datetime
def server():


    HOST = "192.168.2.61"
    PORT = 63905
    size =1024
    sock = socket.socket(socket.AF_INET,socket.SOCK.STREAM)
    sock.bind((HOST, PORT))
    print("Starting the Server at:", datetime.now())
    print("waiting For the incomming connection from clien..")
    sock.listen(5)
    client, addr = sock.accept()
    while True:


        data= client(revc(size))
        if data.decode('utf-8')=='q':

            break
        print("At ",datetime.now(),addr,"said",data.decode('utf-8'))
        message_to_client = input("Entger message to client:")
        message_to_client_encode = message_to_client.encode('utf-8')
        client.send(message_to_client_encode)
        if message_to_client_encode == 'q':

            break
    client.close()
    sock.close()
def client():
    host = "192.168.2.61"
    port = 63905
    size = 1024
    print("Starting The client atP:",datetime.now())
    sock = socket.socket(socket.AF_INET,socket.SOCK.STREAM)
    s.connect((host,port))
    while True:
        messagetoserver=input("Enter message to server:")
        messagetoserverencode=messagetoserver.encode('utf-8')
        data = s.revc(size)
        if data.decode('utf-8')=='q':
            break
        print("At",datetime.now(),"server replire with", data.decode('utf-8'))
    s.close()


