import subprocess
import time 
import server_for_Lisa

def run_command(command):
    text = 'sudo /bin/python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
   
if __name__ == "__main__":
    command = 'osc_server.print_args'
    run_command(command)
    time.sleep(1)