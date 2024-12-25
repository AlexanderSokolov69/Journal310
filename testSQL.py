import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QTableView

app = QApplication(sys.argv)
# db = QSqlDatabase.addDatabase('QSQLITE')
# conn_str = f"""db/database_J2023.db"""
db = QSqlDatabase.addDatabase('QSQLITE')
conn_str = ("Driver={ODBC Driver 17 for SQL Server}" +
            f""";Server=172.16.1.12,1433;Database=Journal4303;uid=sa;pwd=Prestige2011!""")
#conn_str = f"""DSN=it-cube64;uid=sa;pwd=Prestige2011!"""
db.setDatabaseName('db/database_J.db')

if db.open('sa', 'Prestige2011!'):
    print('open database is OK!')
else:
    print(db.lastError().text())
    sys.exit()
# spis = db.tables()
# for n in spis:
#     print(f"{n:16}", end='')
#     sp = []
#     for i in range(db.record(n).count()):
#         sp.append(db.record(n).fieldName(i))
#     print('[', ', '.join(sp), ']')
#
query = QSqlQuery()
query.prepare('select * from users')
query.exec()
model = QSqlTableModel()
model.setTable('users')
model.select()
table = QTableView()
table.setModel(model)

table.show()

sys.exit(app.exec())

# query.next()
# while query.isValid():
#     print(query.value('name'))
#     query.next()
