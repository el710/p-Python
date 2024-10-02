from datetime import datetime
from multiprocessing import Pool

file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line) > 0:
                all_data.append(line)

if __name__ == '__main__':
    ### one process
    start = datetime.now()
    for name in file_list:
        read_info(name)
    end = datetime.now()
    print(f'one process worktime: {end - start}')

    ### multyprocess
    with Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, file_list)    
    end = datetime.now()
    print(f'multyprocess worktime: {end - start}')
