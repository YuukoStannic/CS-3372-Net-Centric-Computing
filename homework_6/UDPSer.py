import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 12000))

print("The server is ready to receive...")
while True:
    data, address = sock.recvfrom(4096)
    print(data)
    sendback = data.upper()
    sendthistoo = str(len(data))
    countwords  = data.split()
    count = str(len(countwords))

    if data:
        sent = sock.sendto(sendback, address)
        sent = sock.sendto(sendthistoo, address)
        sent = sock.sendto(count,address)
        print("sending back data")
