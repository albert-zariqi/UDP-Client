import socket
import re
#Zgjedhja e emrit dhe portit te serverit nga shfrytezuesi
serverName = input("Emri i Serverit: ")
serverPort = input("Numri i Portit: ")

#Ne qofte se shfrytezuesi nuk ka japur emer te serverit atehere merret si default 'localhost'
if(len(serverName) == 0 or serverName == " "):
    serverName = 'localhost'
else:
    serverName = serverName
#Ne qofte se shfrytezuesi nuk ka japur numrin e portit ne te cilin ndegjone serveri, atehere merret si default 11000
if(len(serverPort) == 0 or serverPort == " "):
    serverPort = 11000
    
else:
    serverPort = int(serverPort)
    
#Zgjedhja e protokollit per komunikim, krijimi i nje socket-i
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Kerkesat per te cilat UDP Serveri jone mund te kthej pergjigje 
print("\t\tFAKULTETI I INXHINIERISE ELEKTRIKE DHE KOMPJUTERIKE")
print("===================================================================================\n")
print ("Kerkesat e mundsheme:")
print("\t1.IPADDR,")
print("\t2.PORTNR,")
print("\t3.HOST,")
print("\t4.PRINTO,")
print("\t5.LOJA,")
print("\t6.FIBONACCI,")
print("\t7.KONVERTO,")
print("\t8.ZANORE,")
print("\t9.TIME,")
print("\t10.EKKUADRATIK,")
print("\t11.PALINDROMET,")
print("\t12.ENKRIPTIMI")
print("Ju lutem zgjedheni kerkesen e juaj")
#Mostrat (Pattern) per secilen kerkese
ipReg = "^IPADDR$"
portReg = "^PORTNR$"
zanoreReg = "^ZANORE\s[a-zA-Z\s]+$"
fibReg = "^FIBONACCI\s[0-9]+$"
konReg = "^KONVERTO\s[a-zA-Z]+\s[0-9]+[\.][0-9]+$"
timeReg = "^TIME$"
lojaReg = "^LOJA$"
hostReg = "^HOST$"
printReg = "^PRINTO\s[\w\s]+$"
ekReg = "^EKKUADRATIK\s[-]?[0-9]+\s[-]?[0-9]+\s[-]?[0-9]+$"
enkReg = "^ENKRIPTIMI\s[a-zA-Z\s]+\s[0-9]$"
palReg = "^PALINDROMET\s[a-zA-Z]+$"
#Pjesa kryesore ku kontrollohet kerkesa e klientit, dergohet kerkesa tek serveri si dhe pranimi i pergjigjeve nga serveri
def Main():
        try:
            mesazhi = input("Dergoni kerkesen: ")
            if(re.search(ipReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(portReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(zanoreReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(fibReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(konReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(timeReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(lojaReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(printReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(hostReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(ekReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(enkReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            elif(re.search(palReg,mesazhi)):
                clientSocket.sendto(str.encode(mesazhi),(serverName,serverPort))
                mesazhiPranuar, serverAddress = clientSocket.recvfrom(128)
            else:
                print("Ju lutem shenoni nje kerkese valide!")
                Main()
            print(mesazhiPranuar)
            vazhdim = input("Deshironi kerkese tjeter (shtyp po ose jo)")
            vazhdim = vazhdim.lower()
            if(vazhdim == "po"):
                Main()

        except Exception as err:
            print(err.args)
        clientSocket.close()

#Thirrja e funksionit Main
Main()