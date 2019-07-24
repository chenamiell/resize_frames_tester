import os
import time
from pathlib import Path

import cv2

import settings


class VideoToFrames(object):
    def __init__(self, video_path, fps=0.5, sec=0, count=1):
        self.video_path = video_path
        self.fps = fps
        self.sec = sec
        self.count = count
        self.starting_time = None
        self.ending_time = None
        self.video_name = Path(self.video_path).name.split(".")[0]
        self.images = list()
        self.new_dir_path = None

    def convert_frames(self):
        self.starting_time = time.time()
        vid = cv2.VideoCapture(self.video_path)
        self.new_dir_path = fr'{settings.PROCESSED_VIDEOS}\{self.video_name}'
        if not os.path.exists(self.new_dir_path):
            os.mkdir(self.new_dir_path)
        os.chdir(self.new_dir_path)
        success = self._get_frame(vid)
        while success:
            self.count = self.count + 1
            self.sec = self.sec + self.fps
            self.sec = round(self.sec, 2)
            success = self._get_frame(vid)
        self.ending_time = time.time()

    def _get_frame(self, vid):
        vid.set(cv2.CAP_PROP_POS_MSEC, self.sec * 1000)
        has_frames, image = vid.read()
        if has_frames:
            cv2.imwrite(self.video_name + "_" + str(self.count) + ".jpg", image)
            self.images.append(image)
        return has_frames


