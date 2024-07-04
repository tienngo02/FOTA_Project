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
    user_input = sys.argv[1]

    if user_input == "runningSW":
        print("Run App")

    elif user_input == "activation":
        os.rename(app, backup)
        os.rename(new_SW, app)

    elif user_input == "rollback":
        os.rename(app, new_SW)
        os.rename(backup, app)
        return

    else:
        print("Wrong input")
        return

    # Khởi động tiến trình con và kiểm tra trạng thái ngay lập tức
    try:
        process = subprocess.Popen(['python', app])
        # Kiểm tra ngay nếu tiến trình con đã khởi động thành công
        if process.poll() is None:
            print(f"{app} started successfully.")
        else:
            print(f"{app} failed to start with exit code {process.returncode}.")
    except Exception as e:
        print(f"Failed to start {app}: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_run()
    print("Main program finished.")
