import psycopg2

# Параметры подключения к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="db",  # имя сервиса из docker-compose.yml
    port="5432"
)

cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    department VARCHAR(50)
);
''')

# Вставка данных
cursor.execute("INSERT INTO employees (name, age, department) VALUES ('Alice', 30, 'HR');")
cursor.execute("INSERT INTO employees (name, age, department) VALUES ('Bob', 25, 'Engineering');")
cursor.execute("INSERT INTO employees (name, age, department) VALUES ('Charlie', 35, 'Sales');")

# Сохранение изменений
conn.commit()

# Вывод данных
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

# Закрытие соединения
cursor.close()
conn.close()
