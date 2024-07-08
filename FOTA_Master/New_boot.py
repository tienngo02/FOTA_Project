import os
import subprocess
import sys
import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print(f"Bootloader SW running at: {time.time()}")


scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=2)
scheduler.start()

print()
print("================================")
print("New bootloader is running...")

app = 'App.py'
new_SW = 'New_SW.py'
new_boot = 'New_boot.py'
boot = 'main.py'
backup_app = 'Backup_app.py'
backup_boot = 'Backup_boot'


def get_file_size(file_path):
    file_size = os.path.getsize(file_path)
    return file_size


def main_run():
    user_input = sys.argv[1]

    if user_input == "runningSW":
        print("Run App")

    elif user_input == "activation_boot":
        print("Activation new boot")
        os.rename(boot, backup_boot)
        os.rename(new_boot, boot)
        if get_file_size(app) > 0:
            subprocess.Popen(['python', boot, 'runningSW'])
            return
        else:
            print('App compile fail')

    elif user_input == "rollback_boot":
        print("Rollback boot")
        os.rename(boot, new_boot)
        os.rename(backup_boot, boot)
        if get_file_size(app) > 0:
            subprocess.Popen(['python', boot, 'runningSW'])
            return
        else:
            print('App compile fail')

    elif user_input == "activation":
        print("Activation")
        os.rename(app, backup_app)
        os.rename(new_SW, app)

    elif user_input == "rollback":
        print("Rollback")
        os.rename(app, new_SW)
        os.rename(backup_app, app)
        return

    else:
        print("Wrong input")
        return

    # Khởi động tiến trình con và kiểm tra trạng thái ngay lập tức
    if get_file_size(app) > 0:
        subprocess.Popen(['python', app])
    else:
        print('App compile fail')


if __name__ == '__main__':
    time.sleep(5)
    main_run()
    print("Main program finished.")
    exit()
