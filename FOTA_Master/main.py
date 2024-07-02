import os
import subprocess
import sys

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
        print("Wrong")

    subprocess.Popen(['python', app])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_run()
    print("Bootloader finished.")
    exit()


