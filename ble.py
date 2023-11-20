import bluetooth
import struct
import sys

# change this to the device name you want to advertise
device_name = "my-bluetooth-le-device"

# you can also change this to another address type if needed
addr_type = bluetooth.LE_PUBLIC_ADDRESS

# the Bluetooth SIG assigned UUID for Eddystone-UID
service_uuid = b'\xaa\xfe'

# a random service data (for the Eddystone-UID this is 16 bytes:
# the 12-byte Namespace UUID, and a 4-byte Instance ID)
service_data = b'\x00' * 16

# construct the advertising data
advertising_data = service_uuid + service_data

# get the underlying Bluetooth socket from the standard library
sock = bluetooth.BlueZBluetoothSocket(bluetooth.BLUETOOTH_LE_ADVERTISE)

# bind the socket to the local device address and a randomly selected port
sock.bind((bluetooth.LE_ADVERTISING_ADDRESS,)))

# start advertising the specified service data
sock.send(struct.pack("<BB16sB", 0x02, addr_type, device_name, 0x0a) +
           struct.pack("<BB16s", 0x03, len(advertising_data), advertising_data))

print("Started advertising {}".format(device_name))

# the following loop makes the program run indefinitely, which is typically what you want for a background process
while True:
    # wait for a client to connect to the server socket
    print("Waiting for connection...")
    client, client_info = sock.accept()
    print("Accepted connection from {}".format(client_info))

    # the connection will automatically be closed by the system when the program terminates
