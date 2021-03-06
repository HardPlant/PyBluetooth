import bluetooth
from time import time
from os import system
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock, address = server_sock.accept()

print("Accepted connection from ", address)
while True:
    try:
        data = client_sock.recv(1024)
        print("Received [%s]" % data)
        system(str(data))
        
    except Exception as e:
        print("[{}] {}".format(time(),repr(e)))
    finally:
        client_sock.close()
        server_sock.close()