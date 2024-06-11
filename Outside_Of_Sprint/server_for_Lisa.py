# Huats 2023 oscstarterkit
from pythonosc import osc_server, dispatcher
import subprocess

#global directional_var

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.254.137"
receiver_port = 9000

def process_directional_var(directional_var):
    print(f"Received directional value: {directional_var}")
    
# this function prints the arguments in received OSC messages 
def print_args(addr, *args):
  if addr == "/ext/src/72/p":
    #   text = 'sudo ~/alastair/bin/python3 command.py '
    #   config = text + args[0]
    directional_var = float(args[0])
    process_directional_var(directional_var)
      
    #   try:
    #     output = subprocess.check_output(config, shell=True)
    #     print(output.decode('utf-8'))
    #   except subprocess.CalledProcessError as e:
    #     print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
  
#catches osc messgaes

dispatcher = dispatcher.Dispatcher()

def catcher():
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/print" is received, message_handler function will run """

def server_run():
        server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
        print("serving on{}".format(server.server_address))
        server.serve_forever()
if __name__ == "__main__":
    
    dispatcher.map("/ext/src/72/p", print_args) ## if OSC message with addr "/print" is received, message_handler function will run
    
    server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
    print("serving on{}".format(server.server_address))
    server.serve_forever()