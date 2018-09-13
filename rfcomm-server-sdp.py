'''
Service Discovery Protocol

get_available_port() : get port
advertise_service()
find_service() : search Bluetooth device

Usage:
    bluetooth.get_available_port(protocol) # Deprecated
        returns first available port
        Don't use. go Port 0

    bluetooth.advertise_service(sock, name, uuid)
        bound, listening socket, service name, uuid
        -> while socket closes/stop

    bluetooth.stop_advertising(sock)

    bluetooth.find_service(name=None, uuid=None, bdaddr=None)
        returns list of dict, {host: name: protocol: port}

        look for service with name, uuid
        if bdaddr is None -> all nearby device will be searched
        localhost - locally advertised SDP

'''
import bluetooth
from time import time
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Use SDP
port = 0

server_sock.bind(("",port))
server_sock.listen(1)

# Not works totally, just use uuid
uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
bluetooth.advertise_service(server_sock, "Foobar Service",\
    service_classes=[bluetooth.SERIAL_PORT_CLASS],\
    profiles=[bluetooth.SERIAL_PORT_PROFILE])

while True:
    client_sock, address = server_sock.accept()
    print("Accepted connection from ", address)

    try:
        data = client_sock.recv(1024)
        print("Received [%s]" % data)
    except Exception as e:
        print("[{}] {}".format(time(),repr(e)))
    finally:
        client_sock.close()
        server_sock.close()