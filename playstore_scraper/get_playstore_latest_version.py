import os

from google_play_scraper import app

from lib import env


def main():
    result = app(
        'com.gamingforgood.clashofstreamers',
        lang='en',  # defaults to 'en'
        country='us'  # defaults to 'us'
    )

    with open(os.path.join(env.REPO_PATH, 'playstore_scraper', 'data', 'MomiVersion.txt'), 'w+') as file:
        file.write(result['version'])

    print(result['version'])


if __name__ == "__main__":
    main()
