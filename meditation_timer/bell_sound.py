import os
import time
from concurrent.futures import ThreadPoolExecutor

import pyautogui
from playsound import playsound

MOVE_MOUSE_INTERVAL = 60 * 3
TOTAL_TIME = 60 * 60  # 1 hour
BELL_INTERVAL = 60 * 15  # 15 mins
THREAD_POOL = ThreadPoolExecutor(None)
START = time.time()

BACKGROUND_SOUND = os.path.join(os.getcwd(), '1hour-brown-noise.mp3')
BELL_SOUND = os.path.join(os.getcwd(), 'Meditation-bell-sound.mp3')

pyautogui.FAILSAFE = False


def move_mouse(interval: int = MOVE_MOUSE_INTERVAL):
    """
    Moves the mouse every x seconds to avoid the pc from fallings asleep.
    """

    start = time.time()
    while time.time() - START < TOTAL_TIME:
        if time.time() - start >= interval:
            for i in range(0, 100):
                pyautogui.moveTo(0, i * 5)
            start = time.time()


def background_sound():
    for _ in range(int(TOTAL_TIME / 60) or 2):
        playsound(BACKGROUND_SOUND)


def counter(_round_index: int):
    start = time.time()
    while time.time() - start < 60 * 15:
        time.sleep(1)
        m, s = divmod(60 * 15 - (time.time() - start), 60)
        print(f"Round: {_round_index}. Time Remaining: {int(m)}:{'0' + str(int(s)) if int(s) < 10 else int(s)}")


def bell_sounds():
    for round_index in range(1, int(TOTAL_TIME / BELL_INTERVAL) + 1):
        THREAD_POOL.submit(lambda: playsound(BELL_SOUND))
        counter(round_index)


THREAD_POOL.submit(lambda: background_sound())
_ = input('Press enter when you have warmed up to start the timer.\n\n')
THREAD_POOL.submit(lambda: bell_sounds())
THREAD_POOL.submit(lambda: move_mouse())

index = 0
while time.time() - START < TOTAL_TIME:
    _ = input('Mind wandering?\n\n')

    index += 1
    mind_wandering_ave_interval = int(((time.time() - START) / 60) / index)
    m, s = divmod(time.time() - START, 60)

    print(f"\nMind wandered {index} time(s) in {int(m)}:{'0' + str(int(s)) if int(s) < 10 else int(s)}. Mind Wandering Interval: every {mind_wandering_ave_interval}min(s)\n")
