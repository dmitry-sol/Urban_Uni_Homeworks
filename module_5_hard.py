# module_5_hard
# Дополнительное практическое задание по модулю
import time as t


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

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
        current_user_login = None
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f'Пользователь "{nickname}" - успешный вход')
                current_user_login = 1
                break
            elif nickname == user.nickname and hash(password) != user.password:
                print(f'Пароль {password} не верен, повторите вход')
                current_user_login = 1
                break
        if current_user_login is None:
            print(f'Пользователь "{nickname}" не существует')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
            self.current_user_age = new_user.age
            print(f'Новый пользователь "{new_user}" успешно зарегистрирован')
        else:
            print(f'Пользователь "{nickname}" уже существует')

    def log_out(self):
        print(f'Пользователь "{self.current_user}" покинул UrTube')
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
        if not titles:
            print(f'По вашему запросу "{search_word}" ничего не найдено')
        return titles

    def watch_video(self, title):
        current_video = None
        if self.current_user is not None:
            for video in self.videos:
                if title == str(video):
                    if not video.adult_mode or (self.current_user_age >= 18 and video.adult_mode == True):
                        print(f'Начинаем просмотр "{title}"')
                        current_video = title
                        step = 0
                        while video.time_now < video.duration:
                            t.sleep(0.5)
                            video.time_now += 1
                            step = int(step ** (1 / 2))
                            print(' ' * step, video.time_now, end='')
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
print(ur.get_videos('Абракадабра'))

print('\n= Проверка на вход пользователя и возрастное ограничение =')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

print('\n= Проверка регистрации совпадающего пользователя =')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print('Текущий пользователь: ', ur.current_user)

print('\n= Попытка воспроизведения несуществующего видео =')
ur.watch_video('Лучший язык программирования 2024 года!')

print('\n= Попытка выхода из учетной записи =')
ur.log_out()
print('Текущий пользователь: ', ur.current_user)

print('\n= Проверка на вход зарегистрированного пользователя + возрастное ограничение =')
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')

print('\n= Проверка логики на вход зарегистрированного пользователя c ошибкой ввода =')
ur.log_in('urban_pythonist', 'ScX4vIJClb9YQavjAgF')
ur.log_in('urban_pythonis', 'iScX4vIJClb9YQavjAgF')
