import json

with open('/home/matheus/Code/DickPicMosaic/dataset_v2/sample.json', 'r') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        with open(f'/home/matheus/Code/DickPicMosaic/dataset_v2/samples/{i}.json', 'w') as w:
            json.dump(data, w)