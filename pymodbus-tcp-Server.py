# Import Required Functions from Library

import socket
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Get System IP address and Define Default PORT-502 for Connection
hostname = socket.gethostname()    
server_ip_address = socket.gethostbyname(hostname)
server_port = 2502

# Define Server Perameter
store = ModbusSlaveContext(zero_mode=True)
context = ModbusServerContext(slaves=store, single=True)

# Start Modbus TCP Server
print("[+]Info : Server Started on IP : {I} and PORT : {P} ".format(I=server_ip_address,P=server_port))
StartTcpServer(context, address=(server_ip_address,server_port))