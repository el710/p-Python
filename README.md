On Windows 

1) IDE
   - Setup VS Code
   or 
   - pycharm-community-2024.1.1.exe (from https://www.jetbrains.com/)

2) setup Python interpreter (from python.org)
python-3.12.2-amd64.exe


at terminal

run: python *.py

Python 
*	script language
*	interpreter (python 3. from python.com)
*	environment (PyCharm from JetBrains.com)

PyCharm

setup test project:
*	“pure python” – console application
*	main.py script – make “Hi world” script
*	venv – project type with environment in project directory
*	run with file:  
1.	main.py  - run always main
2.	or current file – run current file

    NumPy — для работы с высокоуровневыми математическими функциями и многомерными массивами. 
    Django и Flask — веб-разработка и веб-приложения (например, Pinterest, YouTube и Instagram написаны на Django).
    SQLAlchemy — для работы с базами данными с применением технологии ORM.
    Cocos2d — мобильные и браузерные игры.
    Tornado — для создания высокопроизводительных приложений, которые способны работать одновременно с сотней тысячей пользователей. 
    Bubot — для программирования робототехники и домашней автоматизации, как вариант — использование на Raspberry Pi.


### https://docs.python.org/
### https://www.youtube.com/watch?v=R4WF9xad_EI - 10 вопросов Python-разработчику
### https://habr.com/ru/companies/ruvds/articles/500296/ - 41 вопрос о работе со строками в Python
### https://www.reg.ru/blog/5-klassnyh-veschej-kotorye-vy-mozhete-osvoit-s-python/ - 5 вещей, которые вы можете освоить с Python


https://www.PyPi.org - site with packets for python with <pip> function:
- pip search <key> - find packet on PyPi.org
- pip install <library><==v.v.v>- install packet with version v.v.v
- pip install -upgrade <><==v.v.v> - ... to version
- pip uninstall <>  - ...
- pip freeze - show list of installed packets
- pip freeze > <filename> - save to file
- pip install -r <filename> - install packets by list in file

packets:
requests - запросить данные с сайта
https://requests.readthedocs.io/en/latest/index.html

pandas - считать данные из файла
https://pandas.pydata.org/docs/user_guide/index.html

numpy - создать массив чисел, выполнить математические операции с массивом
https://numpy.org/doc/stable/user/absolute_beginners.html

matplotlib - визуализировать данные с помощью библиотеки
https://matplotlib.org/stable/users/explain/quick_start.html

pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
https://pillow.readthedocs.io/en/stable/


## Project envirounment:
1. create project directory
2. make virtual envirounment (It keeps project's python interpretator (/scripts) & only used packages)
       
       Use package:
            for vscode we need: > pip install pipenv (vs code may offer to create virtual envirounment...)
            > pipenv shell
            ctrl + shift + p - python select interpreter
            > type python - check set interpreter

      or
      in new project directory
      > python -m venv <venv directory>, venv directory should named 'venv' - common rule

3. Activate project's python interpreter
   venv/Scripts/activate.bat
   if it doesn't work
      - need to restart terminal
      - choose interpretator handly:
   ctrl + shift + p - python select interpreter
   
4. Keep file of used packages with pip - 'requirement.txt'
   pip freeze > <filename> 
   To restore envirounment: pip install -r <filename>
5. make repository
   git init
6. make file for untracked dirs/files
   .gitignore <- /venv, /scripts e.t.c
