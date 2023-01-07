import os

from lib import env
from google_play_scraper import app


result = app(
    'com.gamingforgood.clashofstreamers',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

with open(os.path.join(env.DATA_PATH, 'MomiVersion.txt'), 'w+') as file:
    file.write(result['version'])
