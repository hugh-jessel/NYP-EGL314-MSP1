############ Master Pi -> Slave ############
from pythonosc import osc_server, dispatcher, udp_client

# OSC server settings
receiver_ip = "192.168.254.72"
receiver_port = 23

# OSC client settings
Yamaha = "192.168.254.142"  # IP of the laptop running the GrandMA3Commands.py script
Port = 8000
osc_address = ""

# Function to print received OSC messages and send them
def print_args(addr, *args):
    if addr == "/print":
        received_message = args[0]
        print("Received message:", received_message)
        
        # Send the received message to GrandMA3
        send_message(osc_address, received_message)

# Function to send OSC messages to control GrandMA3
def send_message(address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.UDPClient(Yamaha, Port)

        # Send an OSC message to the GrandMA3 console
        client.send_message(address, message)

        print("Message sent successfully.")
    except:
        print("Unsuccessful")

# Set up OSC dispatcher
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/print", print_args)  # Map "/print" address to print_args function

# OSC server instance
server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("Serving on {}".format(server.server_address))

# Start OSC server
server.serve_forever()

