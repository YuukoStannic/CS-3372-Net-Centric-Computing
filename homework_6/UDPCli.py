import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12000)

while True:
    userdata = raw_input("Please input lowercase sentence")
    sock.sendto(userdata, server_address)
    data, server = sock.recvfrom(4096)
    print(data)
    number, server = sock.recvfrom(4096)
    print(number)
    count, server = sock.recvfrom(4096)
    print(count)

print("Closing socket.")
sock.close()
