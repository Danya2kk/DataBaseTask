import sqlite3


# Функция для создания таблицы
def create_table_employees():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        print("База данных успешно создана и подключена!")

        create_table_query = '''CREATE TABLE IF NOT EXISTS employees (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    position TEXT NOT NULL,
                                    department TEXT NOT NULL,
                                    salary INTEGER NOT NULL
                                );'''
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица успешно создана")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()
            print("База данных закрыта")


# Функия для добавления данных
def insert_data(data):
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        insert_data_query = '''INSERT INTO employees(name, position, department, salary)
                                VALUES (?, ?, ?, ?);
                            '''
        cursor.executemany(insert_data_query, data)
        connection.commit()
        print("Данные успешно добавлены")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для выводы информации
def select_data():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        select_data_query = '''SELECT * FROM employees
                            '''
        cursor.execute(select_data_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для обновления position
def update_position(name, new_position):
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        update_pos = '''UPDATE employees
                        SET position = ?
                        WHERE name = ?
                            '''
        cursor.execute(update_pos, (new_position, name))
        connection.commit()
        print(f"Должность сотрудника {name} успешно обновлена на {new_position}")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для добавления поля HireDate
def add_hire_date_column():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        alter_table_query = '''ALTER TABLE employees
                               ADD COLUMN HireDate TEXT'''
        cursor.execute(alter_table_query)
        connection.commit()
        cursor.close()
        print("Столбец HireDate успешно добавлен")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для обновления данных HireDate
def update_hire_dates(hire_dates):
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        update_query = '''UPDATE employees
                          SET HireDate = ?
                          WHERE id = ?'''
        cursor.executemany(update_query, hire_dates)
        connection.commit()
        cursor.close()
        print("Даты приема на работу успешно обновлены")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для поиска Manager
def find_manager():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        select_query = '''SELECT * FROM employees
                              WHERE position = 'Manager' '''
        cursor.execute(select_query)
        managers = cursor.fetchall()
        cursor.close()
        return managers
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для поиска у кого зп больше 5к
def select_high_salary_employees():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        select_query = '''SELECT * FROM employees
                          WHERE salary > 5000'''
        cursor.execute(select_query)
        high_salary_employees = cursor.fetchall()
        cursor.close()
        return high_salary_employees
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для поиска Sales
def find_sales():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        select_query = '''SELECT * FROM employees
                              WHERE department = 'Sales' '''
        cursor.execute(select_query)
        sales = cursor.fetchall()
        cursor.close()
        return sales
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для средней зп
def get_average_salary():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        select_query = '''SELECT AVG(salary) FROM employees'''
        cursor.execute(select_query)
        average_salary = cursor.fetchone()[0]
        cursor.close()
        return average_salary
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()


# Функция для удаления
def drop_table_employees():
    try:
        connection = sqlite3.connect("employees.db")
        cursor = connection.cursor()
        drop_table_query = '''DROP TABLE employees'''
        cursor.execute(drop_table_query)
        connection.commit()
        cursor.close()
        print("Таблица Employees успешно удалена")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка: ", error)
    finally:
        if connection:
            connection.close()
