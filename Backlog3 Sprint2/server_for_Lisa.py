# Huats 2023 oscstarterkit
from pythonosc import osc_server, dispatcher
import subprocess
import queue
import sys
import socket

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.254.137"
receiver_port = 9000

# this function prints the arguments in received OSC messages 
def print_args(addr, *args):
    global var
    if addr == "/ext/src/72/p":
    #directional_var = float(args[0])
        directional_var = sys.argv
        directional_var.pop(0)
        var = ' '
        for tmp in directional_var:
            if var != ' ':
                var += ' '
            var += tmp
        var += '\n'



""" def close():
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    print ("closed")

# connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(5)
s.connect((receiver_ip,receiver_port))

# send command
s.sendall(var.encode())

# receive a message before closing socket
s.recv(1500)

# close socket
s.close ()
 """
#catches osc messgaes
  
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/ext/src/72/p" is received, message_handler function will run

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on{}".format(server.server_address))
server.serve_forever()

def catcher():
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/print" is received, message_handler function will run



def server_run():
        server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
        print("serving on{}".format(server.server_address))
        server.serve_forever()

""" if __name__ == "__main__":
    
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/print" is received, message_handler function will run
    server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
    print("serving on{}".format(server.server_address))
    server.serve_forever()
    if KeyboardInterrupt:
        print("[!] Keyboard Interrupted!")
        close()
         """


