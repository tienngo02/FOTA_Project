import subprocess
import time
from apscheduler.schedulers.background import BackgroundScheduler

bootloader = "main.py"
arg = "activation"

print("Old SW is running...")


def job():
    print(f"Old SW running at: {time.time()}")


scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=2)
scheduler.start()

time.sleep(5)

subprocess.Popen(['python', bootloader, arg])

exit()
