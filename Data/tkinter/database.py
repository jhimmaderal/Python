import sqlite3

def create_table():
  conn = sqlite3.connect("Employees.db")
  query = conn.cursor()
  query.execute('''
                 CREATE TABLE IF NOT EXISTS Employees (
                   id TEXT PRIMARY KEY,
                   name TEXT
                   role TEXT
                   gender TEXT,
                   status TEXT)''')

  conn.commit()
  conn.close()

def fetch_employee():
  conn = sqlite3.connect('Employees.db')
  query = conn.cursor()
  query.execute('SELECT * FROM Employees')
  employees = query.fetchall()
  conn.close()
  return employees

def insert_employee(id, name, role, gender, status):
  conn = sqlite3.connect('Employees.db')
  query = conn.cursor()
  query.execute('INSERT INTO Employees (id, name, role, gender, status) VALUE (?, ?, ?, ?, ?)',
                (id, name, role, gender, status))
  conn.commit()
  conn.close()

def delete_employee(id):
  conn = sqlite3.connect('Employees.db')
  query = conn.cursor()
  query.execute('DELETE FROM Employees WHERE id = ?', (id))
  conn.commit()
  conn.close()

def update_employee(new_name, new_role, new_gender, new_status, id):
  conn = sqlite3.connect('Employees.db')
  query = conn.cursor()
  query.execute("UPDATE Employees SET name = ?, role = ?, gender = ?, status = ? WHERE id = ?",
                (new_name, new_role, new_gender, new_status, id))
  conn.commit()
  conn.close()

def id_exist(id):
  conn = sqlite3.connect('Employees.db')
  query = conn.cursor()
  query.execute('SELECT COUNT (*) FROM Employees WHERE id = ?', (id,))
  result = query.fetchone()
  conn.close()
  return result[0] > 0

create_table()  