import json
import os
from pprint import pprint

root = './static/galleries'

gallery_map = {}

for gallery, _, imageList in os.walk(root):
    gallery_name = gallery.split('/')[-1]
    if gallery_name != 'galleries':
        gallery_map[gallery_name] = []
        for image in imageList:
            gallery_map[gallery_name].append(image)

for gallery, images in gallery_map.items():
    gallery_map[gallery] = sorted(images)

pprint(gallery_map)

with open('./static/gallery_map.json', 'w+') as map_file:
    map_file.write(json.dumps(gallery_map))
