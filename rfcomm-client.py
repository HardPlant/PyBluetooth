import bluetooth

def get_addr():
    return "0x:0x:0x:0x:0x:0x"

bd_addr = get_addr()

port = 1

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
sock.send("Hello")
sock.close()