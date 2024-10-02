"""
process()
    thread()
    thread()
"""
## using image lib
import multiprocessing.pool
from PIL import Image
from datetime import datetime
"""
make base to work
"""
# for i in range(1, 1001):
#     img = Image.open('./images/foto.jpg').copy()
#     img.save(f'./images/foto_{i:04d}.jpg')

def resize_image(image_file):
    image = Image.open(image_file)
    image = image.resize({700, 600})
    image.save(image_file)


# start = datetime.now()
# for i in range(1, 201):
#     image_file = f'./images/foto_{i:04d}.jpg'
#     resize_image(image_file)
# end = datetime.now()
# print(f'One process time: {end-start}')

"""
multyprocessing...
"""
import multiprocessing

"""
Pool() makes copy of 'main' process, based on file *.py
To avoid running Pool() in duplicate processes
we should be ensure that only '__main__' process 
will use Pool()
...also that is why we comment 'one process' code
"""

if __name__ == '__main__': 

    with multiprocessing.Pool(processes=4) as pool:
        all_images = []
        for i in range(201, 401):
            all_images.append(f'./images/foto_{i:04d}.jpg')
        start = datetime.now()
        pool.map(resize_image, all_images) ## function and iterable list of parameters
    end = datetime.now()
    
    print(f'multy process time: {end-start}')