# Huats 2023 oscstarterkit
# This python script will allow the raspberry pi to act as an OSC server and distribute corresponding OSC messages to the rest of the slave pi in the network
# ywfu-20240521
# To be deployed onto master pi

from pythonosc import osc_server, dispatcher
import osc_client

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.254.49" # Team A
receiver_port = 2003

# this function prints the arguments in received OSC messages
def print_args(addr, *args):
  if addr == "/print":
    print(f"message received {args[0]}")
    msg = args[0]
    var = args[0].split(',')
    spk = int(var[0].strip())
    addr = "/trigger"

    if 1 <= spk <= 3:
       send_addr = "192.168.254.197" #Team C
       send_port = 2001
    elif 4 <= spk <= 6:
      send_addr = "192.168.254.101" #Team E
      send_port = 2002
    elif 7 <= spk <= 9:
      send_addr = "192.168.254.72" #Team B
      send_port = 2003
    elif 10 <= spk <= 12:
      send_addr = "192.168.254.236" #Team F
      send_port = 2004
    
    osc_client.send_message(send_addr, send_port, addr, msg)


#catches osc messgaes
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/print", print_args) ## if OSC message with addr "/print" is received, message_handler function will run

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on{}".format(server.server_address))
server.serve_forever()
