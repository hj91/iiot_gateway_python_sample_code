#example for python modbus library
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.1.6')
d = client.write_register(14,0x0001)
print d
print "Modbus function code",d.function_code
p = client.write_register(14,0x0000)
print p
print "Modbus function code", p.function_code
c = client.read_holding_registers(15,unit = 1)
#c1 = client.read_coils(1,unit = 1) 
print c
#print c1
print c.function_code
client.close()


