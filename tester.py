from time import sleep
import sys
from thread_util.my_thread import MyThread
import os


def test(n, m, video_path):
    thread_list = list()
    for i in range(n):
        t = MyThread(i, video_path)
        t.start()
        thread_list.append(t)
        sleep(m)
    [t.join() for t in thread_list]


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    try:
        val = n
        if val == 0:
            sys.exit("N should be bigger than 0")
    except ValueError:
        sys.exit("N should be integer")

    try:
        val = m
        if val == 0:
            sys.exit("M should be bigger than 0")
    except ValueError:
        sys.exit("M should be integer")

    video_path = sys.argv[3]
    try:
        os.path.isfile(video_path)
    except:
        sys.exit("Vidoe path incorrect")
    test(n, m, video_path)