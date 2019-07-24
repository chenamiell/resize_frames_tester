import sys
from time import sleep
from thread_util.my_thread import MyThread
import os


def test(N, M, video_path):
    thread_list = list()
    for i in range(N):
        t = MyThread(i, video_path)
        t.start()
        thread_list.append(t)
        sleep(M)
    [t.join() for t in thread_list]


if __name__ == '__main__':
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    try:
        val = N
        if (val == 0):
            sys.exit("Error message arg num 1: must be bigger than 0-quitting")
    except ValueError:
        sys.exit("Error message arg num 1: That's not an int!-quitting")

    try:
        val = M
        if (val == 0):
            sys.exit("Error message arg num 2: must be bigger than 0-quitting")
    except ValueError:
        sys.exit("Error message arg num 2: That's not an int!-quitting")

    UPLOAD_FOLDER = sys.argv[3]
    try:
        os.path.isfile(UPLOAD_FOLDER)
    except:
        sys.exit("Error message arg num 3," + UPLOAD_FOLDER + ": That's not a path!-quitting")
    N =1 # sys.argv[1]
    M =10 # sys.argv[2]
    VIDEO_PATH = r'C:\Users\chen amiel\Desktop\1.mp4' #sys.argv[3]
    test(N, M, VIDEO_PATH)