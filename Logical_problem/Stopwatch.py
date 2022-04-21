import time


def StopWatch():
    input("Press enter to start")
    start_time = time.time()
    input("Enter any key to stop the watch")

    stop_time = time.time()

    time_lapsed = stop_time - start_time
    print(time_lapsed)


StopWatch()
