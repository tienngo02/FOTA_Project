import os
import subprocess
import sys
import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print(f"New SW running at: {time.time()}")


scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=2)
scheduler.start()


print()
print("================================")
print("Bootloader is running...")

app = 'App.py'
new_SW = 'New_SW.py'
backup = 'Backup.py'


def main_run():
    status = sys.argv[1]

    if status == "runningSW":
        print("Run App")

    elif status == "activation":
        print('Activation')
        os.rename(app, backup)
        os.rename(new_SW, app)

    elif status == "rollback":
        print('Rollback')
        os.rename(app, new_SW)
        os.rename(backup, app)
    
    else:
        print("Wrong arg")

    subprocess.Popen(['python', app])

    # try:
    #     process = subprocess.Popen(['python', app])
    #     if process.poll() is None:
    #         print(f"Started successfully.")
    #     else:
    #         print(f"{app} failed to start with exit code {process.returncode}.")
    # except Exception as e:
    #     print(f"Failed to start {app}: {e}")


if __name__ == '__main__':
    main_run()
    print("Bootloader finished.")
    exit()
