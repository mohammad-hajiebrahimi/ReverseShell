import socket
import sys

def create_socket():
    global host, port, s
    host = '127.0.0.1'
    port = 8000
    s = socket.socket()
    
def bind_socket():
    try:
        global host, port, s
        s.bind((host, port))
        
        print("bind socket")
        
        s.listen(5)
    except socket.error as msg:
        print(msg)
        bind_socket()
        
def socket_accept():
    con, address = s.accept()
    
    print("connection", address)
    send_command(con)
    con.close()
    
def send_command(con):
    while True:
        cmd = input()
        
        if cmd == 'exit':
            con.close()
            s.close()
            sys.exit()
            
        if len(str.encode(cmd)) > 0:
            con.send(str.encode(cmd))
            recive = str((con.recv(1024), 'utf-8'))
            
            print(recive, end ="")
            
            
def main():
    create_socket()
    bind_socket()
    socket_accept()

 
main()
            