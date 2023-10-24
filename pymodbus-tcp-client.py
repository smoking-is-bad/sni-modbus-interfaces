from pymodbus.constants import Endian
from pymodbus.client import ModbusTcpClient
import socket
import time

#hostname = socket.gethostname()    
server_ip_address = '192.168.1.90'
server_port = 2502

client = ModbusTcpClient(server_ip_address,server_port)

print("[+]Info : Connection : " + str(client.connect()))

for i in range(0,10):
    print(f"[+]Info : Writing Value : {i} On Register : {i} ")
    client.write_registers(i,i)

value = client.read_holding_registers(0,10)
value.registers
