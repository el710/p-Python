'''
Main file
'''
from os import system
from time import sleep

class UrTube:
    users = [] ## list of User's objects
    videos = [] ## list of Video's objects
    current_user = None

    def __init__(self) -> None:
        print("start UrTube application...\n")

    def set_user(self, user):
        UrTube.current_user = user
    
    def log_in(self, nickname, password):
        for i in UrTube.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.set_user(i)
                return True
        return False

    def register(self, nickname, password, age):
        for i in UrTube.users:
            if nickname == i.nickname:
                print(f"Login {nickname} already exists")
                return False
        user = User(nickname, password, age)
        UrTube.users.append(user)
        UrTube.set_user(self, user)
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
            if search.upper() in clip.get_title().upper():
                v_list.append(clip.title)

        if len(v_list) > 0:
            return v_list
        else:
            return None
    
    def get_clip(self, search):
        for clip in UrTube.videos:
            if search == clip.get_title():
                return clip
        return None
          

    def watch_video(self, title):
        if UrTube.current_user == None:
            print("Log in to watch video")
        else:
            scene = UrTube.get_clip(self, title)
            if scene != None:
                if scene.adult_mode and int(self.current_user.old()) < 18:
                    print("This video has age +18 limit")
                else:
                    for i in range(scene.duration):
                        print(i+1)
                        sleep(0.5)
                    print("The end of video")
    
    def exist(self, nickname):
        for i in UrTube.users:
            if i.nickname == nickname:
                return True
        return False

class Video:
    '''
    > Class of user's video <
    '''
    def __init__(self, title, duration, adult_mode=False) -> None:
        self.time_now = 0 ## sec
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
    
    def __str__(self) -> str:
        return f"Clip: {self.title}, length: {self.duration}, start at: {self.time_now}, adult mode: {self.adult_mode}"
    
    def get_title(self):
        return self.title
    
class User:
    '''
    > Class of UrTube's user <
    '''
    def __init__(self, nickname, password, age) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
    def __str__(self) -> str:
        return f"User: {self.nickname}, psw: {self.password}, age: {self.age}\n"
    
    def name(self):
        return self.nickname
    
    def old(self):
        return self.age                                
 

if __name__ == '__main__':

    ur_tube = UrTube()

    v1 = Video("Best programm language of 2024", 200)
    v2 = Video("Why girls need programer?", 10, adult_mode=True)

    ur_tube.add(v1, v2)
    
    print(ur_tube.get_videos('best'))
    print(ur_tube.get_videos('PROG'))

    ur_tube.watch_video("Why girls need programer?")
    ur_tube.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur_tube.watch_video("Why girls need programer?")
    ur_tube.register('urban_pythonist', 'iuhBVGJGj9GJFj', 25)
    ur_tube.watch_video("Why girls need programer?")

    ur_tube.register('vasya_pupkin', 'jbkj&GjvfhJFv', 55)
    
    print(ur_tube.current_user)
    ur_tube.watch_video("Best programm language of 2024!")
    