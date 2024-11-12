from time import sleep

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}, {self.password}, {self.age}'

class Video:

    def __init__(self, title='', duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return isinstance(other, str) and self.title.lower() == other.lower()


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        if self.users.__contains__(nickname) and hash(self.users[nickname].password) == hash(password):
            self.current_user = self.users[nickname]
        else:
            print('Неправильное имя или пароль')

    def register(self, nickname, password, age):
        if self.users.__contains__(nickname):
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users[nickname] = new_user
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not self.videos.__contains__(video.title):
                self.videos[video.title] = video

    def get_videos(self, video_name):
        videos = []
        for video in self.videos.keys():
            if video.lower().__contains__(video_name.lower()):
                videos.append(video)
        return videos

    def watch_video(self, video_name):
        if self.videos.__contains__(video_name):
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                video = self.videos[video_name]
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    time = video.time_now
                    while time < video.duration:
                        time += 1
                        print(time)
                        sleep(1)
                    print('Конец видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')

