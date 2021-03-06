import MySQLdb

#! Открытие соединение с базой данных
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="lab_db"
)
db.set_character_set('utf8')
#! Получить курсор для работы с базой данных
c=db.cursor()

#! Выполнить вставку
c.execute("insert into prodact (prodact_name, description) VALUES (%s, %s);", ('Кефир', '3,5%'))
#! Фиксирование изменений
db.commit()

#! Выполнить выборку
c.execute("select * from prodact;")

#! Забрать все полученные записи
entries = c.fetchall()

#! Распечатать записи
for e in entries:
    print(e)

#! Закрытие курсора
c.close()
#! Закрытие соединения
db.close()