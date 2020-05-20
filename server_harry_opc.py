from opcua import Server
from random import randint


server = Server()

url = "opc.tcp://192.168.1.7:4842"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

temp = Param.add_variable(addspace, "Temp",0)

temp.set_writable()

server.start()

print ("server started at ()".format(url))

while True:
    Temperature = randint(10,50)
    temp.set_value(Temperature)
