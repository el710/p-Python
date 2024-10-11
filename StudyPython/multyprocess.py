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
for i in range(1, 1001):
    img = Image.open('./images/foto.jpg').copy()
    img.save(f'./images/foto_{i:04d}.jpg')

def resize_image(image_file):
    image = Image.open(image_file)
    image = image.resize({700, 600})
    image.save(image_file)

"""
multyprocessing...
"""
import multiprocessing

"""
Pool() makes copy of 'main' process, based on this file <*.py>
it means that every child process will step through all file code with
variables, functions, e.t.c....
To avoid running Pool() in duplicate processes
we should be ensure that only '__main__' process 
will start Pool()
"""
print(f'\n{__name__} start...')
if __name__ == '__main__':
    print(f'MAIN: {datetime.now()}')
    start = datetime.now()
    for i in range(1, 201):
        image_file = f'./images/foto_{i:04d}.jpg'
        resize_image(image_file)
    end = datetime.now()
    print(f'in process time: {end-start}')

    ## make new ONE process...
    with multiprocessing.Pool(processes=4) as pool: ## processes = how much kernel procesors use, not soft-processes
        all_images = []
        for i in range(201, 401):
            all_images.append(f'./images/foto_{i:04d}.jpg')
        start = datetime.now()
        pool.map(resize_image, all_images) ## function and iterable list of parameters
        '''
        map automises work of processes with reliant on count of args
        if args are less then processes then map doesn't use all processes
        '''
    end = datetime.now()
    print(f'new process time: {end-start}')

##-----------------------------------
    def hello(name):
        print(f'Hello {name}')

    pool1 = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool1.map(hello, ['a', 'b'])
    pool1.close()
    pool1.join()
    
##----------------------------------
    print('MAIN: process done')
print(f'\n{__name__} common end...')

# """
# sync processes with queue, pipe...
# """
# from multiprocessing import Pool
# from multiprocessing import Queue
# from multiprocessing import Pipe
# from multiprocessing import Process
# from multiprocessing import Event
# from queue import Empty
# from PIL import Image
# import datetime

# def resize_image(images, queue):
#     for file in images:
#         image = Image.open(file)
#         image = image.resize((800,600))
#         queue.put((file, image))

# def change_color(queue):
#     while True:
#         try:
#             file, image  = queue.get(timeout=5)
#         except Empty:
#             break
#         image = image.convert('L') ## convert to White/Black
#         image.save(file)

# def p_resize_image(images, pipe_end, stop_event):
#     for file in images:
#         image = Image.open(file)
#         image = image.resize((800,600))
#         image.save(file)
#         pipe_end.send(file)
#     stop_event.set()

# def p_change_color(pipe_end, stop_event):
#     while not stop_event.is_set():
#         file  = pipe_end.recv()
#         image = Image.open(file)
#         image = image.convert('L') ## convert to White/Black
#         image.save(file)


# if __name__ == '__main__':
#     ## Queue sinchronize...
#     data = []
#     queue = Queue()

#     for i in range(1, 101):
#         data.append(f'./images/foto_{i:04d}.jpg')
    
#     resize_process = Process(target=resize_image, args=(data, queue))
#     change_process = Process(target=change_color, args=(queue, ))

#     start = datetime.datetime.now()
#     resize_process.start()
#     change_process.start()

#     resize_process.join()
#     change_process.join()
#     end = datetime.datetime.now()
#     print(f'queue sync time: {end - start}')

#     ## pipe synchronize...
#     data = []
#     pipe_end1, pipe_end2 = Pipe()
#     stop_event = Event()

#     for i in range(100, 201):
#         data.append(f'./images/foto_{i:04d}.jpg')
    
#     resize_process = Process(target=p_resize_image, args=(data, pipe_end1, stop_event))
#     change_process = Process(target=p_change_color, args=(pipe_end2, stop_event, ))

#     start = datetime.datetime.now()
#     resize_process.start()
#     change_process.start()

#     resize_process.join()
#     change_process.join()
#     end = datetime.datetime.now()
#     print(f'pipe sync time: {end - start}')

