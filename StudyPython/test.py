import os
import time

os.system('cls')

os.chdir('StudyPython')
directory = os.curdir
print(f"\n Start tree directory: {directory}")


for root, dirs, files in os.walk(directory)                                   : ## walk through directory's tree
    # print(f"\nRoot: {root}")
    # print(f"Directories: {dirs}")
    for file in files:
        full_path = os.path.join(directory, root, file)
        raw_modify_time = os.path.getmtime(full_path)
        modify_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(raw_modify_time))
        
        print(f"""Found file: {file}
            Path: {full_path}
            Size: {os.path.getsize(full_path)} bytes
            Modify time: {modify_time}
            Root dir: {os.path.dirname(full_path)}
            """)