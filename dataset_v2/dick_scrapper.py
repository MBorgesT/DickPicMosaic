import json
import requests
import os
import io
import shutil
from PIL import Image

if os.path.exists('dataset_v2/pics/'):
    shutil.rmtree('dataset_v2/pics/')
os.mkdir('dataset_v2/pics/')

subreddits = ['penis', 'softies', 'balls', 'ratemycock', 'dicks', 'averagepenis', 'MassiveCock', 'tinydick']
sub_ids = ['t5_2qlsu', 't5_2thzp', 't5_2qqmk', 't5_2xd8b', 't5_2rl3k', 't5_2w0o4', 't5_2t2qe', 't5_2sr8s']
dataset_path = '/media/matheus/26af0b06-54ad-4402-99f9-2e9972be25a2/matheus/dick-datasets/RS_2020-11'
print('Scrapping images...')
with open(dataset_path, 'r') as f:
    for line in f:
        post = json.loads(line)
        if post['subreddit'] in subreddits and post['author'] != '[deleted]' and post['url'][-4:] == '.jpg':
            try:
                img_data = requests.get(post['url'], timeout=12).content
                post_id = post['id']
                img = Image.open(io.BytesIO(img_data)).resize((60, 60))
                img.save(f'dataset_v2/pics/{post_id}.jpg')
                os.remove('dataset_v2/temp.jpg')
            except Exception:
                pass