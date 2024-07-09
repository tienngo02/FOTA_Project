try:
    import subprocess
    import sys
    import time
    from apscheduler.schedulers.background import BackgroundScheduler

    bootloader = "main.py"
    arg = "rollback"

    print("New SW is running...")


    def job():
        print(f"New SW running at: {time.time()}")


    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=2)
    scheduler.start()

    time.sleep(5)
    pri('TEST ROLLBACK')
    print("TEST")
    exit()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    subprocess.Popen(['python', bootloader, arg])


