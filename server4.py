import socket 
import sys
import ipaddress
import select

s= socket.socket()
print("Socket Successfully Created")

host = str(ipaddress.ip_address(sys.argv[1]))
port = int(sys.argv[2])

s.bind((host,port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listining")

inputs = [s]

while True:
    in_fd,out_fd,err_fd = select.select(inputs,inputs,[],5)
    for fd in in_fd:
        if fd == s:
            c , addr = s.accept()
            print ('Got connection from', addr)
            inputs.append(c)
            
        elif fd:
            eq = fd.recv(1024).decode()
            if eq:
                if eq == "q":
                    fd.sendall("quit".encode('utf-8'))
                    inputs.remove(fd)
                
                print("Received: {}" .format(eq))
                fd.sendall(eq.encode('utf-8'))
            else:
                fd.close()
                inputs.remove(fd)