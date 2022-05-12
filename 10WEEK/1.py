import psycopg2
import random

conn = psycopg2.connect(
    host = 'localhost',
    database = 'db',
    user = 'Amirchik1',
    password = '123456'
)
running  = True
while running:
    print('Commands: insert | update | query | delete | exit')
    command = input()

    if command == 'insert' or command == '/i':
        insert_type = input('Choose insert option: terminal | file\n')
        if insert_type == 'terminal' or insert_type == '/t':
            user = input('input text in format \'user, 7-777-777-77-77\'\n')
            user = user.split(', ')
            sql = f"insert into phonebook (name, number) values ('{user[0]}','{user[1]}');"
        elif insert_type == 'file' or insert_type == '/f':
            with open('phoneBook.csv', 'r') as f :
                data = f.readlines()
            for i in range(len(data)) :
                data[i] = data[i].removesuffix('\n')
                data[i] = f"({data[i]})"

            sql = f"insert into phonebook (name,number) values {','.join(data)};"

    elif command == 'update' or command == '/u':
        update_type = input('Choose what to update: name | phone\n')
        if update_type == 'name' or update_type == 'n':
            phone = input('Enter phone of the user\n')
            new_name = input('Enter the new name you want to set\n')
            sql = f'''
                update phonebook
                set name = \'{new_name}\'
                where number = \'{phone}\'
            '''
        elif update_type == 'phone' or update_type == '/p':
            name = input('Enter name of the user\n')
            new_phone = input('Enter the new phone number you want to set\n')
            sql = f'''
                update phonebook
                set number = \'{new_phone}\'
                where name = \' {name}\'
            '''

    elif command == 'query' or command == '/q':
        user = input('Enter name or phone of the user you want to find\n')
        if user == '/all' :
            sql = '''
                select *
                from phonebook
            '''
        else :
            sql = f'''
                select *
                from phonebook
                where name = \'{user}\' or number = \'{user}\'
            '''

    elif command == 'delete' or command == '/d':
        user = input('Enter name or phone of the user you want to delete\n')
        if user == '/all' :
            sql = '''
                delete from phonebook
                where id > 0
            '''
        else :
            sql = f'''
                delete from phonebook
                where name = \'{user}\' or number = \'{user}\'
            '''
    elif command == 'exit' or command == '/e' :
        running = False

    if command != 'exit' and command != '/e' :
        cursor = conn.cursor()
        cursor.execute(sql)
        if command == 'query' or command == '/q':
            result = cursor.fetchall()
            if len(result) > 0 :
                for i in result :
                    print(f'{i[0]}, {i[1]}')
            else :
                print('There is no such user')
        else :
            conn.commit()

        cursor.close()

conn.close()