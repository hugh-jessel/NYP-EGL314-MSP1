# Huats 2023 oscstarterkit
from pythonosc import osc_server, dispatcher
import subprocess

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.254.72"
receiver_port = 23

# this function prints the arguments in received OSC messages 
def print_args(addr, *args):
  if addr == "/print":
      text = 'sudo /bin/python3 command.py '
      config = text + args[0]
      print(config)
      try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
      except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
        
#catches osc messgaes
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/print", print_args) ## if OSC message with addr "/print" is received, message_handler function will run

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on{}".format(server.server_address))
server.serve_forever()
  

