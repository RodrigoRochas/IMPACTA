import pyodbc

conex = pyodbc.connect (
                        'Driver=SQL Server;'
                        'Server=DESKTOP-UOTL7NU;'
                        'Database=HELLO;'
                        'Trusted_Connection = yes;'
                        )

cursor = conex.cursor()

cursor.execute("SELECT * FROM TBL_CIDADES")

row = cursor.fetchone()
res = []
while row:
    for column in row:
        res.append(column)
        
    print(res)
    res = []
    row = cursor.fetchone()