import os
import time
import logging
import datetime
import re
import sys

import plotly.graph_objects as go

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

LATEST_WANDER_COUNT = 0


def create_html_graph():
    files = os.listdir(logs_path)

    mind_wandering_data = {}
    for file in sorted(files):
        with open(os.path.join(logs_path, file), 'r') as f:
            lines = f.readlines()
            for line in reversed(lines):
                if 'Mind wandered' in line:
                    times = int(re.search(r'Mind wandered (\d+) ', line).group(1))
                    mind_wandering_data[file.replace('.log', '')] = times
                    break
                else:
                    mind_wandering_data[file.replace('.log', '')] = 0

    # Create a bar chart
    print(list(mind_wandering_data.keys()))
    fig = go.Figure([go.Bar(x=list(mind_wandering_data.keys()), y=list(mind_wandering_data.values()))])
    # Set titles
    fig.update_layout(title_text='Mind Wandering', xaxis_title='Date', yaxis_title='Times', xaxis_type='category', height=800)
    # Save as HTML
    html_path = os.path.join(env.REPO_PATH, 'meditation_timer', 'mind_wandering_graph.html')
    fig.write_html(html_path)

    html_lines = ''
    with open(html_path, "r") as f:
        html_lines = f.read()

    html_lines = """
    <ul>
        <li>Wandering for more than 2 seconds counts as mind wandering</li>
        <li>If I can't remember where a thought started then it counts as mind wandering</li>
        <li>If I remember where it started and it felt like less than 2 seconds then it doesn't count as mind wandering (it only counts as a distraction)</li>
    </ul>
    """ + html_lines

    with open(html_path, "w") as f:
        f.write(html_lines)


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
    global LATEST_WANDER_COUNT
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
        LATEST_WANDER_COUNT = index
        logging.info(f"\nMind wandered {index} time(s) in {int(m)}:{'0' + str(int(s)) if int(s) < 10 else int(s)}. Mind Wandering Interval: every {mind_wandering_ave_interval}min(s)\n")


if __name__ == "__main__":
    try:
        main()
    except:
        logging.info("\n\nEnding session\n\n")
        THREAD_POOL.shutdown(wait=False)
        create_html_graph()
        os.system('pkill -9 -f "python -m meditation_timer.bell_sound"')
        os._exit(1)
