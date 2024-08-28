# module_5_hard
# Дополнительное практическое задание по модулю
import time as t


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_nick_pass(self):
        return self.nickname, self.password

    def __eq__(self, other):
        return other.nickname == self.nickname

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return other.title == self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.current_user_age = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, password) == user.get_nick_pass():
                self.current_user = user
                return user
            else:
                print(f'Пользователь {nickname} не найден, пройдите регистрацию\n')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
            self.current_user_age = new_user.age
        else:
            print(f"Пользователь "{nickname}" уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in str(self.videos):
                self.videos.append(video)
                print(f'Видео "{video.title}" успешно загружено')
            else:
                print(f'Видео с именем "{video.title}" уже существует')

    def get_videos(self, search_word):
        titles = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                titles.append(video)
        return titles

    def watch_video(self, title):
        current_video = None
        if self.current_user is not None:
            for video in self.videos:
                if title == str(video):
                    if not video.adult_mode or (self.current_user_age >= 18 and video.adult_mode == True):
                        print(f'Начинаем просмотр "{title}"')
                        current_video = title
                        i = 0
                        t1 = 0
                        while i < video.duration:
                            t.sleep(0.5)
                            i += 1
                            t1 = int(t1 ** (1 / 2))
                            print(' ' * t1, i, end='')
                        print(' = Конец видео =')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        current_video = title
                        break
            if current_video is None:
                print(f'Видео с именем "{title}" не существует')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = (Video('Для чего девушкам парень программист?', 10, adult_mode=True))

print('\n= Добавление видео =')
ur.add(v1, v2)
ur.add(v3)

print('\n= Проверка поиска =')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

print('\n= Проверка на вход пользователя и возрастное ограничение =')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

print('\n= Проверка входа в другой аккаунт =')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print('Текущий пользователь: ', ur.current_user)

print('\n= Попытка воспроизведения несуществующего видео =')
ur.watch_video('Лучший язык программирования 2024 года!')
