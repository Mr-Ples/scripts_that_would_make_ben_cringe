import os
import time
import logging
import sys
import datetime

from concurrent.futures import ThreadPoolExecutor

import pyautogui
from playsound import playsound

from lib import env

logs_path = '/home/simonl/meditation_logs/meditation_timer/logs/'
os.makedirs(logs_path, exist_ok=True)
today = datetime.datetime.now().strftime("%Y-%m-%d")
log_path = os.path.join(env.REPO_PATH, logs_path, f'{today}.log')
targets = logging.StreamHandler(sys.stdout), logging.FileHandler(log_path, 'a+')
logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=targets)

MOVE_MOUSE_INTERVAL = 60 * 3
THREAD_POOL = ThreadPoolExecutor(None)
START = time.time()

BACKGROUND_SOUND = os.path.join(env.REPO_PATH, 'meditation_timer', '1hour-brown-noise.mp3')
BELL_SOUND = os.path.join(env.REPO_PATH, 'meditation_timer', 'Meditation-bell-sound.mp3')
pyautogui.FAILSAFE = False


def move_mouse(total: int, interval: int = MOVE_MOUSE_INTERVAL):
    """
    Moves the mouse every x seconds to avoid the pc from fallings asleep.
    """

    start = time.time()
    while time.time() - START < total:
        if time.time() - start >= interval:
            # for i in range(0, 100):
            #     pyautogui.moveTo(0, i * 5)
            pyautogui.moveTo(0, 15)
            start = time.time()


def background_sound(total: int):
    for _ in range(int(total / 60) or 2):
        playsound(BACKGROUND_SOUND)


def counter(_round_index: int):
    start = time.time()
    while time.time() - start < 60 * 15:
        time.sleep(1)
        m, s = divmod(60 * 15 - (time.time() - start), 60)
        logging.info(f"Round: {_round_index}. Time Remaining: {int(m)}:{'0' + str(int(s)) if int(s) < 10 else int(s)}")


def bell_sounds(total: int, interval: int):
    for round_index in range(1, int(total / interval) + 1):
        THREAD_POOL.submit(lambda: playsound(BELL_SOUND))
        counter(round_index)


def main(total: int = 60 * 60, interval: int = 60 * 15):
    """
    Meditation timer.
        - plays background sound
        - plays bel at given interval
        - counts down time between each interval
        - tapping enter indicates mind wandering

    :param total: total meditaion time in minutes. Defaults to 1 Hour
    :param interval: bell interval in minutes. Defaults to 15 mins
    """

    logging.info("\n\nStarting session\n\n")
    THREAD_POOL.submit(lambda: background_sound(total))
    _ = input('Press enter when you have warmed up to start the timer.\n\n')
    THREAD_POOL.submit(lambda: bell_sounds(total, interval))
    THREAD_POOL.submit(lambda: move_mouse(total))

    index = 0
    while time.time() - START < total:
        _ = input('Mind wandering?\n\n')

        index += 1
        mind_wandering_ave_interval = int(((time.time() - START) / 60) / index)
        m, s = divmod(time.time() - START, 60)

        logging.info(f"\nMind wandered {index} time(s) in {int(m)}:{'0' + str(int(s)) if int(s) < 10 else int(s)}. Mind Wandering Interval: every {mind_wandering_ave_interval}min(s)\n")


if __name__ == "__main__":
    main()
