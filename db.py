import pymysql

USER = 'root'
PASSWORD = 'mysql'
DATABASE = 'cursed'
HOST='localhost'
CHARSET='utf8mb4'
CURSORCLASS=pymysql.cursors.DictCursor
CONNECTION = '0'

def authorize():
    print(f'Введите имя пользователя: ')
    global USER
    USER = input()
    print(f'Введите пароль: ')
    global PASSWORD
    PASSWORD = input()
    print(f'Введите название базы данныз: ')
    global DATABASE
    DATABASE = input()
    try:
        create_connection()
        print('Успешно')
        return 1
    except pymysql.Error as e:
        print('Ошибка ', e)

def create_connection():
        global CONNECTION
        CONNECTION = pymysql.connect(host=HOST,
                                    user=USER,
                                    password=PASSWORD,
                                    database=DATABASE,
                                    charset=CHARSET,
                                    cursorclass=pymysql.cursors.DictCursor)

def base_select():
    try:
        with CONNECTION.cursor() as cursor:
            sql = input()
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    except pymysql.Error as e:
        print("Ошибка ", e)

"""main"""
print('Добро пожаловать в модуль управления SQL')
authorized = 0
while True:
    print('Нажмите 1 для авторизации пользователя')
    print('Нажмите 2 для выполнения запроса')
    print('Нажмите 404 для выхода')
    statement = int(input())
    if statement==1:
        authorized = authorize()
    elif statement==2 and authorized:
        base_select()
    elif statement==404:
        print('пока')
        break
    else:
        print('error')
    
else:
    CONNECTION.close()
