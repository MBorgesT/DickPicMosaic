from praw import Reddit
import requests
import os.path
from alive_progress import alive_bar
import shutil


def create_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

create_dir('raw_pics/')

with open('creds.txt', 'r') as f:
    id, secret = [x.replace('\n', '') for x in f.readlines()]

reddit = Reddit(
    client_id=id,
    client_secret=secret,
    user_agent='Pets Bot',
)
reddit.read_only = True

subreddits = ['penis', 'softies', 'balls', 'ratemycock', 'dicks', 'averagepenis', 'MassiveCock', 'tinydick']
posts_per_sub = 2500

with alive_bar(len(subreddits) * posts_per_sub) as bar:
    for sub_name in subreddits:
        create_dir(f'raw_pics/{sub_name}/')
        sub = reddit.subreddit(sub_name)
        for post in sub.new(limit=posts_per_sub):
            if post.url[-4:] == '.jpg':
                try:
                    img_data = requests.get(post.url, timeout=12).content
                    with open(f'raw_pics/{sub_name}/{post.id}.jpg', 'wb') as handler:
                        handler.write(img_data)
                except Exception:
                    pass
            bar()