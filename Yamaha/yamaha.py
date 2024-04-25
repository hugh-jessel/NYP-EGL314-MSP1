
# This python file works with the Raspberry Pi
# Please ensure that this python script is in the same directory as command.py and recall.py
# Huats 2023 oscstarterkit
# Please refer to Yamnaha's command_list.pdf to get the full list of control
# There are two functions in this python script, namely, run_command and run_recall (specifically to recall scene)
# A valid input argument for run_command would be 'set MIXER:Current/InCh/Fader/Level 0 0 1000' - this will execute the command for the console adjust channel 1's fader to +10dB
# A valid input argument for run_recall would be '8' - this will execute the command for the console to recall scene 8

import subprocess
import time 
import osc_server

def run_command(command):
    text = 'sudo /bin/python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

'''def run_recall(command):
    text = 'python3 recall.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:

print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")'''
        
'''def fader(ip_addr, port, x, y):
    command = "set MIXER:Current/InCh/Fader/Level" + {x} + " 0 " + {y}
    run_command(command)'''
    
if __name__ == "__main__":
    command = 'osc_server.print_args'
    print(command)
    run_command(command)
    time.sleep(1)
