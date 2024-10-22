import socket
target_host = "127.0.0.1"  # This should be the IP address
target_port = 80            # This should be the port number
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"AABBCC", (target_host, target_port))
response, addr = client.recvfrom(1024)
print(response)
