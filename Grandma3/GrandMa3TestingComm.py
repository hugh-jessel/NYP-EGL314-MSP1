# from pythonosc import udp_client
# import time

# def send_message(receiver_ip, receiver_port, address, message):
# 	try:
# 		# Create an OSC client to send messages
# 		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

# 		# Send an OSC message to the receiver
# 		client.send_message(address, message)   

# 		print("Message sent successfully.")
# 	except:
# 		print("Unsuccesful")

# #change the below values
# if __name__ == "__main__":
#     LAPTOP_IP = "192.168.254.142"		# send to laptop w grandMA3
#     PORT = 8000                     # laptop w grandMA3 port number
#     addr = "/gma3/cmd/"				# Keep it as it is


#     send_message(LAPTOP_IP, PORT, addr, "Go+ Exec 202 Executor 201 At 0")  #Commands to control the Playback and other Gma3 controls


# # Huats 2023 oscstarterkit
# from pythonosc import osc_server, dispatcher
# 
# # change the receiver_ip value to your RPi's IP address
# receiver_ip = "192.168.254.142"
# receiver_port = 8000
# 
# # this function prints the arguments in received OSC messages 
# def print_args(addr, *args):
#   if addr == "/print":
#     print(args[0])
#   
# #catches osc messgaes
# dispatcher = dispatcher.Dispatcher()
# dispatcher.map("/print", print_args) ## if OSC message with addr "/print" is received, message_handler function will run
# 
# server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
# print("serving on{}".format(server.server_address))
# server.serve_forever()
# 
# 
# 
#




############ Master Pi -> Slave ############
from pythonosc import osc_server, dispatcher, udp_client

# OSC server settings
receiver_ip = "192.168.254.137"
receiver_port = 23

# OSC client settings
laptop_ip = "192.168.254.142"  # IP of the laptop running the GrandMA3Commands.py script
grandma3_port = 8000
osc_address = "/gma3/cmd/"

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
        client = udp_client.SimpleUDPClient(laptop_ip, grandma3_port)

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

