import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
     )
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
# Конец требуемой части кода предыдущей задачи.

# Начало новой задачи.
cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
number_of_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]

print(f'Средний баланс всех пользователей: {sum_balance / number_of_users}')

# Обнуление базы данных для удобства проверок.
# cursor.execute('DELETE FROM Users')

connection.commit()
connection.close()
