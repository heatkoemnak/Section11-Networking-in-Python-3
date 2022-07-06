import socket
sock = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
port = 63905
sock.connect(('192.168.2.61'),port)
msg = sock.revc(1024)
msg_decoded =msg.decode('utf-8')
print("Message from server:"+ msg_decoded)
msg_back=input("Do you want to Respond to the server? ")
msg_back_encode=msg_back.encode("utf-8")
sock.send(msg_back_encoded)