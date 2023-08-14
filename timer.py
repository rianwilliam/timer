import time

def stopwatch(t):
    limit = 0
    while limit <= t:
        mins, secs = divmod(limit, 60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        limit += 1

    print("Time completed")

t = input("Enter the time in seconds: ")

stopwatch(int(t))
