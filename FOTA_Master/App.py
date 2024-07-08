import subprocess
import time
import json
from apscheduler.schedulers.background import BackgroundScheduler

bootloader = "main.py"
arg = "activation"

print("Old SW is running...")

JSONFILE = 'Version_information_file.json'

class version_file_control:
    data = None

    def __init__(self):
        with open(JSONFILE, 'r') as file:
            self.data = json.load(file)
         
    def read_2latest_version(self, file_name):
        return self.data[file_name]['running'], self.data[file_name]['non-running']
        
    def update_version(self):
        return 


def Download_NewSW():
    print("Downloading new software...")
    time.sleep(3)
    return True


def job():
    print(f"Old SW running at: {time.time()}")


scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=5)
scheduler.start()


while True:
    user_input = input('Enter command (e.g., "App,1.1"): ')
    split_input = user_input.split(',')

    if len(split_input) < 2:
        print('Invalid input format. Please use "Command,Version" format.')
        continue

    command, version = split_input[0], split_input[1]

    try:
        version = float(version)
    except ValueError:
        print('Invalid version number. Please enter a valid number.')
        continue

    Version_file_control = version_file_control()

    if command == 'App':
        running, non_running = Version_file_control.read_2latest_version('FOTA_Master_App')
        if version > running and version > non_running:
            print("Comparing with two latest versions in FOTA Master")
            if Download_NewSW():
                print("Download new software success")
                Version_file_control.update_version('FOTA_Master_App', version)
                subprocess.Popen(['python', bootloader, arg])
                exit()

    elif command == 'Bootloader':
        print('todo')

    elif command == 'Client':
        print('todo')

    else:
        print('Error: Unrecognized command.')

    time.sleep(1)

    # user_input = input('Enter command: ')
    # split_input = user_input.split(',')

    # Version_file_control = version_file_control()

    # if split_input[0] == 'App':
    #     running, non_running = Version_file_control.read_2latest_version('FOTA_Master_App')
    #     if float(split_input[1]) > running and split_input[1] > non_running :
    #         print("Compare with two latest version in FOTA Master")
    #         if Download_NewSW():
    #             print("Download new software success")
    #             subprocess.Popen(['python', bootloader, arg])
    #             exit()

    # elif split_input[0] == 'Bootloader':
    #     print('todo')

    # elif split_input[0] == 'Client':
    #     print('todo')
        
    # else:
    #      print('Error')
    