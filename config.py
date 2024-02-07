import pymysql

TOKEN = '6566067886:AAGgoXMx9LDKo2ONQ69v7mF4p8u_GAYPckE'

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'fc_db',
    'autocommit': True,
}

# Создаем таблицу команд, если ее нет
connection = pymysql.connect(**db_config)
with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams(
            id CHAR(36) NOT NULL DEFAULT UUID(),
            name VARCHAR(255) NOT NULL,
            PRIMARY KEY (id)
            ) ENGINE=INNODB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4
    """)
