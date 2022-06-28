import time

import opcua.ua
from opcua import Server

serverName = "test"
endpoint = "opc.tcp://127.0.0.1:5757/" + serverName
ns1 = "Room1"
server = Server()

def StartServer():

    server.set_server_name(serverName)
    server.set_endpoint(endpoint)
    server.register_namespace(ns1)

    object = server.get_objects_node()
    print(object)
    var1 = object.add_object('ns=2;i=3000', "OP100")
    att1 = var1.add_variable('ns=2;i=3138', "TrackingID", " 0000315622S031T")
    att0 = var1.add_variable('ns=2;i=0', "testConsoElec0", 0)
    att133 = var1.add_variable('ns=2;i=1', "testConsoElec1", 1)
    att2 = var1.add_variable('ns=2;i=2', "testConsoElec2", 2)
    att3 = var1.add_variable('ns=2;i=3', "testConsoElec3", 3)
    att4 = var1.add_variable('ns=2;i=4', "testConsoElec4", 4)
    att5 = var1.add_variable('ns=2;i=5', "testConsoElec5", 5)
    att6 = var1.add_variable('ns=2;i=6', "testConsoElec6", 6)
    att7 = var1.add_variable('ns=2;i=7', "testConsoElec7", 7)
    att8 = var1.add_variable('ns=2;i=8', "testConsoElec8", 8)
    att10 = var1.add_variable('ns=2;i=10', "testConsoElec", 10)
    att11 = var1.add_variable('ns=2;i=11', "testConsoElec", 11)
    att12 = var1.add_variable('ns=2;i=12', "testConsoElec", 12)
    att13 = var1.add_variable('ns=2;i=13', "testConsoElec", 13)
    att14 = var1.add_variable('ns=2;i=14', "testConsoElec", 14)
    att15 = var1.add_variable('ns=2;i=15', "testConsoElec", 15)
    att16 = var1.add_variable('ns=2;i=16', "testConsoElec", 16)
    att17 = var1.add_variable('ns=2;i=17', "testConsoElec", 17)
    att18 = var1.add_variable('ns=2;i=18', "testConsoElec", 18)
    att19 = var1.add_variable('ns=2;i=19', "testConsoElec", 19)
    att20 = var1.add_variable('ns=2;i=20', "testConsoElec", 20)
    att21 = var1.add_variable('ns=2;i=21', "testConsoElec", 21)
    att22 = var1.add_variable('ns=2;i=22', "testConsoElec", 22)
    att23 = var1.add_variable('ns=2;i=23', "testConsoElec", 23)
    att24 = var1.add_variable('ns=2;i=24', "testConsoElec", 24)
    att25 = var1.add_variable('ns=2;i=25', "testConsoElec", 25)
    att26 = var1.add_variable('ns=2;i=26', "testConsoElec", 26)
    att27 = var1.add_variable('ns=2;i=27', "testConsoElec", 27)
    att28 = var1.add_variable('ns=2;i=28', "testConsoElec", 28)
    att29 = var1.add_variable('ns=2;i=29', "testConsoElec", 29)
    att30 = var1.add_variable('ns=2;i=30', "testConsoElec", 30)
    att31 = var1.add_variable('ns=2;i=31', "testConsoElec", 31)
    att32 = var1.add_variable('ns=2;i=32', "testConsoElec", 32)
    att33 = var1.add_variable('ns=2;i=33', "testConsoElec", 33)
    att34 = var1.add_variable('ns=2;i=34', "testConsoElec", 34)
    att35 = var1.add_variable('ns=2;i=35', "testConsoElec", 35)
    att36 = var1.add_variable('ns=2;i=36', "testConsoElec", 36)
    att37 = var1.add_variable('ns=2;i=37', "testConsoElec", 37)
    att38 = var1.add_variable('ns=2;i=38', "testConsoElec", 38)
    att39 = var1.add_variable('ns=2;i=39', "testConsoElec", 39)
    att40 = var1.add_variable('ns=2;i=40', "testConsoElec", 40)
    att41 = var1.add_variable('ns=2;i=41', "testConsoElec", 41)
    att42 = var1.add_variable('ns=2;i=42', "testConsoElec", 42)
    att43 = var1.add_variable('ns=2;i=43', "testConsoElec", 43)
    att44 = var1.add_variable('ns=2;i=44', "testConsoElec", 44)
    att45 = var1.add_variable('ns=2;i=45', "testConsoElec", 45)
    att46 = var1.add_variable('ns=2;i=46', "testConsoElec", 46)
    att47 = var1.add_variable('ns=2;i=47', "testConsoElec", 47)
    att48 = var1.add_variable('ns=2;i=48', "testConsoElec", 48)
    att49 = var1.add_variable('ns=2;i=49', "testConsoElec", 49)

    print(att1.get_value())
    print(att2.get_value())
    print(att3.get_value())


    print("Starting Server ...")
    server.start()
    print("SERVER STARTED / Endpoint : " + endpoint + " / Server Name : " + serverName)
    print("\n---Namespaces---")
    print(server.get_namespace_array())
    print("\n---Commands---")
    print("q : Quit","\nns : Show namespaces","\ns : Search (Just enter namespace, it will display each node)")

StartServer()

relaunchCommand = True
while(relaunchCommand):
    command = input("\n>>> ")

    if(command == ('q' or 'Q')):
        #for i in [0, 1, 2]:
        #    print(".", end = ' ')
        #    time.sleep(1)
        relaunchCommand = False
        server.stop()
    elif(command == "ns"):
        print("\n---Namespaces---")
        print(server.get_namespace_array())
    elif(command == "s"):
        inputNamespace = input("Enter Namespace >>>")
        print(server.get_node('ns=2;i=3138'))
    else:
        relaunchCommand = True

