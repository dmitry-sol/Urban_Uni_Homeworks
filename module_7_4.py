# module_7_4.py
# "Форматирование строк".

name1 = '"Мастер кода"'
name2 = '"Волшебники данных"'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
winner = ''
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 2)

print('В команде %s участников: %s!' % (name1, team1_num))
print('В команде %s участников: %s!' % (name2, team2_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда {} решила задач: {}!'.format(name1, score_1))
print('Команда {} решила задач: {}!'.format(name2, score_2))
print('{} решили задачи за {} с!'.format(name1, team1_time))
print('{} решили задачи за {} с!'.format(name2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    winner = name1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    winner = name2
else:
    challenge_result = 'Ничья!'

challenge_result = f'Победа команды {winner}!'
print(challenge_result)
