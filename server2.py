import socket
import sys
import ipaddress
import threading     

s = socket.socket()
print ("Socket Successfully Created")

host = str(ipaddress.ip_address(sys.argv[1]))
port = int(sys.argv[2])

s.bind((host,port))
print("Socket binded to %s"%(port))

s.listen(5)
print ("Socket is listining")

#list of connection from client
threads = []

def calc(c,addr):
    th_id = threading.get_ident()
    print('Thread id: {} connection from address: {}'.format(th_id,addr))
    while True:
        try:
            eq = c.recv(1024).decode()
            if eq == "q":
                c.sendall("quit".encode('utf-8'))
                break
            else:
                print("Equation is:",eq)
                re = eval(eq)
                c.sendall(str(re).encode('utf-8'))
        except (ZeroDivisionError):
            c.sendall("div-by-zero".encode('utf-8'))
                    
    c.close()    

while True:
    c,addr = s.accept()
    new_th = threading.Thread(target=calc,args=(c,addr)) #target is function
    threads.append(new_th)
    new_th.start() #staring thread

for thread in threads:
    thread.join() #working concurrently

s.close()
