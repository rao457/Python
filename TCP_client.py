import socket
#CREATING TCP CLIENT
# data_to_send= "Hello server it is sample data"
# target_host = "www.google.com"
# target_port = 80
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((target_host, target_port))
# client.send(data_to_send.encode('utf-8'),  (target_host, target_port))
# response = client.recv(4096)
# print(response.decode('utf-8'))
#CREATING UDP CLIENT
TARGET_HOST = '126.1.1.0'
TARGET_PORT = 23
data_to_sent = "aabbcc"
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_client.sendto(data_to_sent.encode('utf-8'),                                                                                                                  (TARGET_HOST, TARGET_PORT))
data , addr = socket_client.recvfrom(4096)
print(data)