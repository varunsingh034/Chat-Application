import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.221.8"
port = 1234
complete = (ip_add, port)
message =input("kya msg kroge ")
encode_mgs=message.encode('ascii')
s.sendto(encode_mgs,complete)
