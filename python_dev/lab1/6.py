import schedule
import time
import datetime

def say_ku():
    now = datetime.datetime.now().hour
    for i in range(1, now + 1):
        print("Ку")

schedule.every().hour.at(":00").do(say_ku)

while True:
    schedule.run_pending()
    time.sleep(1)
