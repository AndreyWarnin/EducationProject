team1_name = 'Маги'
team2_name = 'Волшебники'
team1_num = 5
team2_num = 3
score_1 = 13
score_2 = 11
team1_time = 868.57
team2_time = 955.149
tasks_total = team1_num + team2_num
time_avg = (team1_time + team2_time) / tasks_total

# Форматирование: %
string1 = 'В команде %s участников: %s!' % (team1_name, team1_num)
string2 = 'Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num)

# Форматирование: .format
string3 = 'Команда {} решила задач: {}'.format(team2_name, score_2)
string4 = '{team1} решили задачи за {time1} с'.format(team1=team1_name, time1=team1_time)

# Форматирование: f
string5 = f'Команды решили {score_1} и {score_2} задач'

challenge_result = None
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team1_name}'
elif score_2 > score_1 or score_2 == score_1 and team2_time < team1_time:
    challenge_result = f'Победа команды {team2_name}'
else:
    challenge_result = 'Ничья'

string6 = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} за задачу!'

print(string1)
print(string2)
print(string3)
print(string4)
print(string5)
print(challenge_result)
print(string6)