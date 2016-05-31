'''
Generate thousands of icons of graphs by parallel computing
CPU intense: multi-processing
IO intense: multi-threading
'''
import os
import time
import PIL # Python Image Lib
from multiprocessing import Pool
from PIL import Image
SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f.lower())

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)

if __name__ == "__main__":
    start_time = time.time()
    folder = os.path.abspath('./image_data') # use your own data set
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))
    images = get_image_paths(folder)
    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()
    print str(time.time() - start_time)
