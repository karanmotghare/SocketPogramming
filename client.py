import socket             
import ipaddress
import sys
# Create a socket object 
s = socket.socket()         
  
try:
    host = str(ipaddress.ip_address(sys.argv[1]))     # Reading IP Address
    port = int(sys.argv[2])                           # Reading port number
    s.connect((host, port))                           # Connecting to server
    print("IP address is:", host)
    print("port number is:", port)
    print("Connected to server")

    while(True):
        equ=input("equation in form (e.g., '9 + 8', '4 / 2', '4 * 7'). or q to quit: ")
        s.sendall(equ.encode('utf-8'))
        result = s.recv(1024).decode()

        if result == "quit":
            print("Closing client connection, goodbye take care have a nice day")
            break
        elif result == "div-by-zero":
            print("can't divide by 0")
        else:
            print("Server replied Answer is:", result)
            
    s.close()
    
except (IndexError, ValueError):
    print("You did not specify an IP address and port number")
# Define the port on which you want to connect 
#port = 12345                
# connect to the server on local computer 
#s.connect(('127.0.0.1', port)) 
# receive data from the server 
#print (s.recv(1024) )
# close the connection 
#s.close()     