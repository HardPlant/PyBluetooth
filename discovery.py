import bluetooth

target_name = "Galaxy J7"
target_address = None
# 한번에 찾아지지 않을 수 있음
nearby_devices =  bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print("current ", bdaddr, bluetooth.lookup_name(bdaddr))
    if target_name == bluetooth.lookup_name(bdaddr) :
        target_address = bdaddr
        break

if target_address is not None:
    print("Target Address:", target_address)
else:
    print("Not found")