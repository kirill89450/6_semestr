import schedule
import time
import datetime

def say_ku(message, silent_range):
    now = datetime.datetime.now().hour
    start, end = map(int, silent_range.split("-"))
    if start <= now < end:
        return
    for i in range(1, now + 1):
        print(message)

message = input("Введите своё сообщение: ")
silent_range = input("Введите молчаливые период (пример 00-07): ")

schedule.every().hour.at(":00").do(say_ku, message, silent_range)

while True:
    schedule.run_pending()
    time.sleep(1)
