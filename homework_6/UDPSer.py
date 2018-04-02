import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 12000))
message = 0

print("The server is ready to receive...")
while True:
    data, address = sock.recvfrom(4096)
    rtnsender = data.decode()
    upper = rtnsender.upper()
    stringlength = str(len(rtnsender))
    message+= 1
    print("The received " + str(message)  +" from client is " + rtnsender + " the length of message is " + stringlength)
    
    sendback = "The number of characters in the inputted string " + upper + " is " + stringlength

    if data:
        sent = sock.sendto(sendback.encode(), address)
