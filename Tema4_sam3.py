import datetime
import time


def print_current_time_for_5_seconds():
    for i in range(5):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)


if __name__ == '__main__':
    print_current_time_for_5_seconds()