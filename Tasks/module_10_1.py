from threading import Thread
from time import sleep
from datetime import datetime
from os import system

system('cls')

# def decor(func):
#     def wrapper(count, file):
#         print(f'{datetime.now()}: ', end=' ')
#         func(count, file)        
#     return wrapper

# @decor
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for idx in range(1, word_count + 1):
            file.write(f'Some word N {idx}\n')
            sleep(0.1)
    print(f'Writing to file <{file_name}> is over')

start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = datetime.now()
print(f"Time work of {write_words.__name__}(): {finish_time - start_time}") 

thread_1 = Thread(target=write_words, args=(10, 'example5.txt', ))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt', ))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt', ))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt', ))

start_time = datetime.now()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
finish_time = datetime.now()
print(f"Time work of threads: {finish_time - start_time}") 

