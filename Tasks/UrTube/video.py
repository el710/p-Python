from os import system

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


if __name__ == '__main__':
    system('cls')
    print("start video mudule...")
    print(Video.__doc__)
    testclip = Video("Test", 5)
    print(testclip)