import pyodbc, pandas as pd

connection = pyodbc.connect('Driver={SQL Server};' 
                      'Server=DESKTOP-QNHJ5Q7\SQLEXPRESS;'
                      'Database=db1;'
                      'Trusted_Connection=yes;')

query = pd.read_sql_query("""SELECT * FROM customers""", connection)
type(query)

cursor = connection.cursor()
cursor.execute('SELECT TOP 100 * FROM customers')

for i in cursor:
    print(i)

cursor.close()
