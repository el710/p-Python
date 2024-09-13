import os

# pathdir = "Temp"

data = os.walk(".")
_num = 1
for _, _, _files in data:
    for _filename in _files:
        search_id = f"{_num:02d}"
        print(_filename, search_id)
        if search_id in _filename:
            newname = f"Bluye 1-{search_id}.mp4"
            os.rename(_filename, newname)
            _num += 1
            print(newname)
