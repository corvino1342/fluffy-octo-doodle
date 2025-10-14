from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import os

def save_tiles(img, msk, out_dir, img_name):
    count = 0
    skipped = 0
    for i in range(0, height, tile_measure):
        for j in range(0, width, tile_measure):
            count += 1

            box = (j, i, j + tile_measure, i+ tile_measure)
            mask_tile = msk.crop(box)

            if mask_tile.size != (tile_measure, tile_measure) or mask_tile.getextrema() == ((0,0),(0,0),(0,0)):
                skipped += 1
                continue

            image_tile = img.crop(box)
            image_tile.save(out_dir + f'/{img_name}_{count}.tiff')

            mask_tile.save(out_dir + f'_labels/{img_name}_{count}.tif')
    print(f'{img_name} DONE! --- tiles skipped: {skipped}/{count} ({(100 * skipped/count):.1f}%)')

training_maps = ['22678915_15', '22678930_15', '22678945_15',
                 '22678960_15', '22678975_15', '22678990_15']

validation_maps = ['22978945_15']

testing_maps = ['22828930_15', '22828990_15']

tile_measure = 128
width, height = (1500, 1500)

# TRAINING
print('TRAINING MAPS')
for name in training_maps:

    os.makedirs('datasets/tiles/train/', exist_ok=True)
    os.makedirs('datasets/tiles/train_labels/', exist_ok=True)

    image = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/train/{name}.tiff')
    mask = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/train_labels/{name}.tif')

    save_tiles(image, mask, 'datasets/tiles/train', name)

# VALIDATION
print('VALIDATION MAPS')

for name in validation_maps:

    os.makedirs('datasets/tiles/val/', exist_ok=True)
    os.makedirs('datasets/tiles/val_labels/', exist_ok=True)

    image = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/val/{name}.tiff')
    mask = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/val_labels/{name}.tif')

    save_tiles(image, mask, 'datasets/tiles/val', name)

# TESTING
print('TESTING MAPS')

for name in testing_maps:

    os.makedirs('datasets/tiles/test/', exist_ok=True)
    os.makedirs('datasets/tiles/test_labels/', exist_ok=True)

    image = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/test/{name}.tiff')
    mask = Image.open(f'datasets/massachusetts-buildings-dataset/tiff/test_labels/{name}.tif')

    save_tiles(image, mask, 'datasets/tiles/test', name)