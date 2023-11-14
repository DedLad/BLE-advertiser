import pygattlib
from pygattlib.uuid import Uuid
import time

class MyBLEDevice:
    def __init__(self, address, name):
        self.adapter = pygattlib.BGAPIBackend(serial_port="hci0")
        self.adapter.start()
        self.device = self.adapter.connect(address)
        self.name = name

    def spam_advertisement(self):
        advertisement_uuid = Uuid("1809") # The BLE Service UUID
        manufacturer_uuid = Uuid("2A29") # The Manufacturer UUID
        device_name_uuid = Uuid("2A00") # The Device Name UUID

        # Infinite loop to keep advertising
        while True:
            # Read the Manufacturer data
            manufacturer_data = self.device.char_read(manufacturer_uuid)
            print("Manufacturer Data: ", manufacturer_data)

            # Write the device name
            self.device.char_write(device_name_uuid, self.name)

            # Sleep for 5 seconds
            time.sleep(5)

airpods = MyBLEDevice("AIRPODS_MAC_ADDRESS", "AirPods")
jbl_headphones = MyBLEDevice("JBL_HEADPHONES_MAC_ADDRESS", "JBL Headphones")

airpods.spam_advertisement()
jbl_headphones.spam_advertisement()