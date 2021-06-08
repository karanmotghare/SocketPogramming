import socket 
import sys
import ipaddress

s = socket.socket()
print ("Socket Successfully Created")

#Reading from command line
host = str(ipaddress.ip_address(sys.argv[1]))
port = int(sys.argv[2])

#binding
s.bind((host,port))
print ("Socket binded to %s" %(port))

#listining
s.listen(5)
print ("Socket is listining")

#loop till ctrl + c
while True: 
    #accepting connection
    c, addr = s.accept()     
    print ('Got connection from', addr )
    while True:
        try:
            eq = c.recv(1024).decode()
            if eq == "q":
                c.sendall("quit".encode('utf-8'))
                break
            else:
                print("Equation is:",eq)
                #evaluating equation
                re = eval(eq)
                c.sendall(str(re).encode('utf-8'))
        except (ZeroDivisionError):
            c.sendall("div-by-zero".encode('utf-8'))
                    
    c.close()
        
s.close()
#    c.sendall('Thank you for connecting'.encode('utf-8'))
#    c.close() 
