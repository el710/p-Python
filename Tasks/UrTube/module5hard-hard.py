'''
Main file
'''
from os import system
from user import User
from video import Video
from time import sleep

class UrTube:
    users = [] ## list of User's objects
    videos = [] ## list of Video's objects
    current_user = None

    def __init__(self) -> None:
        print("start UrTube application...\n")

    def __del__(self) -> None:
        print(f"UrTube app for {UrTube.current_user} is stopped")

    def set_user(self, nickname):
        UrTube.current_user = nickname
    
    def log_in(self, nickname, password):
        for i in UrTube.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.set_user(nickname)
                return True
        return False

    def register(self, nickname, password, age):
        for i in UrTube.users:
            if nickname == i.nickname:
                return False
        
        UrTube.users.append(User(nickname, password, age))
        UrTube.set_user(self, nickname)
        return True
        

    def log_out(self):
        UrTube.current_user = None


    def add(self, *args):
        for i in args:
           clip_exits = False
           for clip in UrTube.videos:
              if i.title == clip.title:
                  clip_exits = True
            
           if not clip_exits:
              UrTube.videos.append(i)
    

    def get_videos(self, search = ''):
        v_list = []
        for clip in UrTube.videos:
            if search.upper() in clip.title.upper():
                v_list.append(clip)
        if len(v_list) > 0:
            return v_list
        else:
            return None
    
    def get_title(number):
        if number > 0 and number <= len(UrTube.videos):
            return UrTube.videos[number - 1].get_title()
        else:
            return '' 
           

    def watch_video(self, title):
        if title != '':
            lin = '-' * len(title)
            user = None

            ## find video & User
            for i in UrTube.users:
                if i.nickname == UrTube.current_user:
                    user = i
            scene = UrTube.get_videos(self, title)

            if scene[0].adult_mode and int(user.old()) < 18:
                print("This video has age +18 limit")
            else:
                for i in range(scene[0].duration):
                    system('cls')
                    print(f"\n-------- {scene[0].title} --------")
                    print(f"|")
                    print(f"|         {i+1} scene from {scene[0].duration}")
                    print(f"|")
                    print(f"----------{lin}--------")
                    sleep(1)
            
            input("\nPress <Enter> to exit")
        else:
            print(f"Video was't found...")
            sleep(2)
    
    def exist(self, nickname):
        for i in UrTube.users:
            if i.nickname == nickname:
                return True
        return False
                    
    def show_desk(self):
        num = 1
        print("\n-------- List of videos --------")
        for clip in UrTube.videos:
            print(f"[{num} - {clip.title} ]")
            num += 1
        print("--------------------------------\n")
        
    
    def start(self, mode='welcome'):
        menu = menu_welcome = "<1> - login, <2> - registration, <Enter> - exit"
        menu_login = "<Enter> - back"
        menu_desk = "<1> - find video, <2> - watch video, <Enter> - back"
        find_result = None
        query = new_login = new_password = command = current_video = None
        
        def set_mode(new_mode, clear_log = True):
            nonlocal mode, menu, query, new_login, new_password, command
            if clear_log:
                new_login = new_password = command = None

            mode = new_mode
            if new_mode == 'welcome':
                menu = menu_welcome
                query = "input mode> "
            elif new_mode == 'login':
                menu = menu_login
                query = "input login> "
            elif new_mode == 'log_name':
                menu = menu_login
                query = "input password> "                
            elif new_mode == 'reg':
                menu = menu_login
                query = "input login> "
            elif new_mode == 'reg2':
                menu = menu_login
                query = "input password> "
            elif new_mode == 'reg3':
                menu = menu_login
                query = "input your age> "
            elif new_mode == 'desk':
                menu = menu_desk
                query = "input mode> "
            elif new_mode == 'search':
                menu = menu_login
                query = "input string to search> "
            elif new_mode == 'choose':
                menu = menu_login
                query = "input number of video> "
            else:
                mode = None
        
        set_mode(mode)
                
        while True:
            if mode == 'welcome':
                if command == '':
                    mode = None
                elif command == '1':
                    set_mode('login')
                elif command == '2':
                    set_mode('reg')

            elif mode == 'login':
                if command  == '':
                    set_mode('welcome')
                else:
                    if not self.exist(command):
                        print(f"User {command} not exists")
                        sleep(2)
                        set_mode('welcome')
                    else:
                        new_login = command
                        set_mode('log_name',clear_log=False)
            elif mode == 'log_name':
                if command  == '':
                    set_mode('welcome')
                else:
                    new_password = command
                    if self.log_in(new_login, new_password):
                        set_mode('desk')
                    else:
                        print(f"Wrong password")
                        sleep(2)
                        set_mode('welcome')
                
            
            elif mode == 'reg':
                if command  == '':
                    set_mode('welcome')
                else:
                    if self.exist(command):
                        print(f"Login {command} is busy")
                        sleep(2)
                        set_mode('welcome')
                    else:
                        set_mode('reg2', clear_log=False)
                        new_login = command
            elif mode == 'reg2':
                if command  == '':
                    set_mode('welcome')
                else:
                    set_mode('reg3', clear_log=False)
                    new_password = command
            elif mode == 'reg3':
                if command  == '':
                    set_mode('welcome')
                else:
                    if self.register(new_login, new_password, command):
                        set_mode('desk')
                    else:
                        set_mode('welcome')
            elif mode == 'desk':
                if command  == '':
                    self.log_out()
                    set_mode('welcome')
                elif command == '1':
                    set_mode('search')
                elif command == '2':
                    set_mode('choose')
            elif mode == 'search':
                if command  == '':
                    set_mode('desk')
                else:
                    find_result = self.get_videos(command)
                    if find_result == None:
                        print("No clip was found")
                        sleep(2)
            elif mode == 'choose':
                if command == '':
                    set_mode('desk')
                elif int(command) <= 0 or int(command) > len(UrTube.videos):
                    print("Wrong number. Try again")
                    sleep(2)
                else:
                    self.watch_video(UrTube.get_title(int(command)))
                    set_mode('desk')

                    
            ## show mode screen
            if mode == None:
                break;
            else:
                system('cls')
                if UrTube.current_user != None:
                    print(f"UrTube: Welcome {UrTube.current_user}")
                else:
                    print(f"UrTube: Welcome")
                
                self.show_desk()
                
                if find_result != None:
                    for i in range(len(find_result)):
                        print("Found: ", find_result[i])
                    find_result = None
                
                print(menu)
                command = input(query)
                                
 

if __name__ == '__main__':

    ur_tube = UrTube()

    video_welcome = Video("Welcome to UrTube", 5)
    v1 = Video("Best proramm language of 2024", 20)
    v2 = Video("Why girls need programer?", 10, adult_mode=True)
    ur_tube.add(video_welcome, v1, v2)

    ur_tube.start()
    print(*UrTube.users)
    print(*UrTube.videos)


    