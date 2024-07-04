import socket
from pythonosc import osc_server, dispatcher

receiver_ip = "192.168.254.137"

receiver_port = 9000

def close():
    
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    print ("closed")
    
""" # connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(5)
s.connect((receiver_ip,receiver_port))

# receive a message before closing socket
s.recv(1500)
# close socket
s.close ()
 """
if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/ext/src/72/p" is received, message_handler function will run
    
    server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
    print("serving on{}".format(server.server_address))
    server.serve_forever()
    if KeyboardInterrupt:

        print("[!] Keyboard Interrupted!")
        close()