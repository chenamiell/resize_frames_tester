import threading
import time
from os import listdir
from os.path import isfile, join
from pprint import pprint

import requests

import settings
from video_to_frames.convert_video_to_frames import VideoToFrames


class MyThread(threading.Thread):
    def __init__(self, threadID, video_path):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.video_path = video_path
        self.responses = list()
        self.start_time = None
        self.end_time = None

    def run(self):
        self.start_time = time.time()
        v2f = VideoToFrames(video_path=self.video_path)
        v2f.convert_frames()
        dir_files = [f for f in listdir(v2f.new_dir_path) if isfile(join(v2f.new_dir_path, f))]

        for file in dir_files:
            files = {'image': open(file, 'rb')}
            self.responses.append(requests.post(url=settings.URL, files=files))
        self.end_time = time.time()

        pprint(
            {
                'insatnces_response': [r.json() for r in self.responses],
                'whole_video_frames_resized': self.end_time - self.start_time
            }
        )