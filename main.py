"""1. Представим, что у нас есть таблица "Employees" с полями
"Name", "Position", "Department", "Salary".
• Создайте таблицу "Employees" с указанными полями.
• Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
• Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
• Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
• Добавьте записи о дате приема на работу для всех
сотрудников.
• Найдите всех сотрудников, чья должность "Manager".
• Найдите всех сотрудников, у которых зарплата больше 5000
долларов.
• Найдите всех сотрудников, которые работают в отделе
"Sales".
• Найдите среднюю зарплату по всем сотрудникам.
• Удалите таблицу "Employees\""""

import sqlite3
import employees as emp

'''Создание таблица employyes'''
# emp.create_table_employees()

'''Вставка в таблицу нескольких записей'''
# data = [
#     ('Alice', 'Developer', 'IT', 6000),
#     ('Bob', 'Manager', 'Sales', 7000),
#     ('Charlie', 'Developer', 'IT', 5500),
#     ('David', 'Intern', 'Marketing', 3000),
#     ('Eve', 'Manager', 'HR', 7500)
# ]
#
# emp.insert_data(data)
# print(emp.select_data())

'''Обновление информации о должности'''
# emp.update_position('Alice', 'Senior Developer')
# print(emp.select_data())

'''Добавление поля HireDate и добавление записей в HireDate'''
# emp.add_hire_date_column()
#
# hire_dates = [
#     ('2021-01-15', 1),
#     ('2019-03-20', 2),
#     ('2020-07-01', 3),
#     ('2023-01-05', 4),
#     ('2018-11-30', 5)
# ]
#
# emp.update_hire_dates(hire_dates)
# print(emp.select_data())

'''Вывод сотрудников чья должность Manager'''
# print(emp.find_manager())

'''Вывод сотрулников у кого зп > 5000'''
# print(emp.select_high_salary_employees())

'''Вывод сотрудников в отделе Sales'''
# print(emp.find_sales())

'''Вывод информации о средней зп'''
# print(emp.get_average_salary())

'''Удаление таблицы'''
# emp.drop_table_employees()
