# Файл module_3_2

message1 = 'Это сообщение для проверки связи'
recipient1 = 'vasyok1337@gmail.com'

message2 = 'Вы видите это сообщение как лучший студент курса!'
recipient2 = 'urban.fan@mail.ru'
sender2 = 'urban.info@gmail.com'

message3 = 'Пожалуйста, исправьте задание'
recipient3 = 'urban.student@mail.ru'
sender3 = 'urban.teacher@mail.uk'

message4 = 'Напоминаю самому себе о вебинаре'
recipient4 = 'urban.teacher@mail.ru'
sender4 = 'urban.teacher@mail.ru'

def send_email(message_, recipient_, sender_='university.help@gmail.com'):
    if sender_ == recipient_:
        print(f'Нельзя отправить письмо самому себе!')
    elif (recipient_.find('@') == -1 or sender_.find('@') == -1 or recipient_.endswith(
        (".ru", ".net", ".com")) is False or
          sender_.endswith((".ru", ".net", ".com")) is False):
        print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')
    elif sender_ != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender_} на адрес {recipient_}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender_} на адрес {recipient_}')
    return


send_email(message1, recipient1)
send_email(message2, recipient2, sender2)
send_email(message3, recipient3, sender3)
send_email(message4, recipient4, sender4)
