# module_5_hard
# Дополнительное практическое задание по модулю
import time as t


class User:
    def __init__(self, nickname, password, age=0):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, user=[], videos=[]):
        self.user = list(user)
        self.videos = list(videos)
        self.current_user = {}

    def __hash__(self):
        return hash(self.password)

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        ur.user.append({'nickname': self.nickname, 'password': self.password, 'age': self.age})
        ur.current_user = {'nickname': self.nickname, 'password': self.password, 'age': self.age}

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        global n
        global p
        global j
        n = ''
        p = ''
        j = -1
        for i in ur.user:
            j += 1
            if hash(i['nickname']) == hash(self.nickname):
                n = i['nickname']
                p = i['password']
                break
        if not n:
            print(f'Пользователь {self.nickname} не найден, пройдите регистрацию\n')
        elif p != self.password:
            print('Неверный пароль\n')
        else:
            print(f'Вход выполнен, {nickname}')
            ur.current_user = self.user[j]

    def add(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        if int(self.adult_mode) == 1:
            self.adult_mode = True
        else:
            self.adult_mode = False
        ur.videos.append({'title': self.title, 'duration': self.duration, 'time_now': self.time_now,
                          'adult_mode': self.adult_mode})

    def get_videos(self, search_word):
        self.search_word = search_word.lower()
        global fnd, lst
        lst = ''
        fnd = ''
        for i in ur.videos:
            fnd = i['title'].lower().find(self.search_word)
            if fnd >= 0:
                lst = i['title']
                print('По вашему запросу есть совпадение: Найден фильм: ', lst)
        if lst == '':
            print('Ничего не найдено')

    def watch_video(self, title, *args):
        self.title = title
        global ttl, ti, a, am
        ttl = ''
        ti = 0
        a = ''
        am = False
        if ur.current_user != {}:
            if ur.current_user['age'] >= 18:
                am = True
            for i in ur.videos:
                if i['title'] == self.title:
                    ttl = i['title']
                    a = i['adult_mode']
                    ti = i['duration']
                    if not a or a == am == True:
                        print('Начало просмотра видео:')
                        i = 0
                        t1 = 0
                        while i < ti / 10:
                            t.sleep(0.5)
                            i += 1
                            t1 = int(t1 ** (1 / 2))
                            print(' ' * t1, i, end='')
                        print(' = Конец видео =')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def log_out(self):
        ur.current_user = {}


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 50, adult_mode=True)
ur.add(v1.title, v1.duration)
ur.add(v2.title, v2.duration, adult_mode=v2.adult_mode)

while True:
    choice = input('Выберите действие: \n'
                   '1 - Войти в учетную запись\n'
                   '2 - Зарегистрироваться\n'
                   '3 - Добавить видео в видеотеку\n'
                   '4 - Найти видео\n'
                   '5 - Проиграть видео\n'
                   '6 - Выйти из учетной записи\n'
                   '7 - Выйти\n')
    if choice == str(1):
        user = User(input('Ведите логин: '), input('Введите пароль: '))
        ur.log_in(user.nickname, user.password)
        print()
    elif choice == str(2):
        user = User(input('Ведите логин: '), input('Введите пароль: '), int(input('Введите ваш возраст: ')))
        ur.register(user.nickname, user.password, user.age)
        print()
    elif choice == str(3):
        # v = Video(input('Введите заголовок: '), int(input('длительность: ')), time_now=0,
        #           adult_mode=input('Введите 1 если 18+, иначе 0: '))
        ur.add(input('Введите заголовок: '), int(input('Длительность: ')), time_now=0,
               adult_mode=input('Введите 1 если 18+, иначе 0: '))
        print()
    elif choice == str(4):
        ur.get_videos(input('Введите название фильма: '))
        print()
    elif choice == str(5):
        ur.watch_video(input('Введите название фильма: '))
        print()
    elif choice == str(6):
        ur.log_out()
        print()
    elif choice == str(7):
        break
    else:
        continue
