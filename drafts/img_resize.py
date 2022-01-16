import os
import shutil
from PIL import Image
from alive_progress import alive_bar

if os.path.exists('resized_pics_200/'):
    shutil.rmtree('resized_pics_200/')
os.mkdir('resized_pics_200/')

directories = os.listdir('raw_pics/')
n_files = 0
for dir in directories:
    n_files += len(os.listdir(f'raw_pics/{dir}/'))

with alive_bar(n_files) as bar:
    for dir in directories:
        files = os.listdir(f'raw_pics/{dir}/')
        for f in files:
            try:
                new_img = Image.open(f'raw_pics/{dir}/{f}').convert('RGB').resize((200, 200))
                new_img.save(f'resized_pics_200/{f}')
            except Exception:
                pass
            bar()