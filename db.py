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
        print('Авторизация прошла успешно')
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
            for res in result:
                print(res)
    except pymysql.Error as e:
        print("Ошибка ", e)

def show_grants():
    try:
        with CONNECTION.cursor() as cursor:
            sql = f"SHOW GRANTS FOR '{USER}'@'localhost';"
            cursor.execute(sql)
            result = cursor.fetchall()
            for res in result:
                print(res)
    except pymysql.Error as e:
        print("Ошибка ", e)

def create_user():
    try:
        with CONNECTION.cursor() as cursor:
            print(f'Введите имя нового пользователя: ')
            user = input()
            print(f'Введите пароль нового пользователя: ')
            password = input()
            sql = f"CREATE USER '{user}'@'localhost' IDENTIFIED BY '{password}';"
            cursor.execute(sql)
            result = cursor.fetchall()
            for res in result:
                print(res)
            print('Пользователь успешно создан')
    except pymysql.Error as e:
        print("Ошибка ", e)

def give_grants():
    try:
        with CONNECTION.cursor() as cursor:
            print(f'Введите имя пользователя: ')
            user = input()
            print(f'Введите комманды для доступа в формате: "cmd1, cmd2, etc."')
            commands = input()
            print(f'Введите название таблицы')
            table = input()
            sql = f"grant {commands} ON {DATABASE}.{table} TO '{user}'@'localhost';"
            cursor.execute(sql)
            result = cursor.fetchall()
            for res in result:
                print(res)
            print('Права выданы')
    except pymysql.Error as e:
        print("Ошибка ", e)


print('Добро пожаловать в модуль управления SQL')
authorized = 0
while True:
    print('Нажмите 1 для авторизации пользователя')
    if authorized:   
        print('Нажмите 2 для выполнения запроса')
        print('Нажмите 3 для просмотра своих прав')
        print('Нажмите 4 чтобы создать нового пользователя')
        print('Нажмите 5 чтобы выдать права пользователю')
    print('Нажмите 404 для выхода')
    statement = input()
    print("\033[H\033[J")
    if statement=='1':
        authorized = authorize()
    elif statement=='2' and authorized:
        base_select()
    elif statement=='3' and authorized:
        show_grants()
    elif statement=='4' and authorized:
        create_user()
    elif statement=='5' and authorized:
        give_grants()
    elif statement=='404':
        print('выход из программы')
        break
    else:
        print('error')
    
else:
    CONNECTION.close()
