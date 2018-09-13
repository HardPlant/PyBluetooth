import bluetooth

def get_addr():
    return "0x:0x:0x:0x:0x:0x"

bd_addr = get_addr()

port = 1

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
while True:
    try:
        sock.send("Hello")
        data = sock.recv(1024)
        print("Received: \n[%s]" % data)
    finally:
        sock.close()