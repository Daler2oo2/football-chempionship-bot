import pymysql

TOKEN = 'your bot token'

db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'pass',
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
