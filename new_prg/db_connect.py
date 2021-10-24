import sys
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication

from classes.cl_const import Const
from classes.cl_logwriter import LogWriter


class TSqlQuery(QSqlQuery):
    prepare_str = ''
    def __init__(self, params=None, dsort=None):
        super(TSqlQuery, self).__init__()
        self.flog = LogWriter()
        self.param_str = []
        self.sort_str = ''
        self.cashe = []
        if params:
            self.set_param_str(params)
        if dsort:
            self.set_sort_str(dsort)

    def set_param_str(self, spis=None):
        self.param_str = spis

    def set_sort_str(self, sort=None):
        if sort:
            self.sort_str = sort

    def refresh_select(self):
        super().finish()
        if self.sort_str:
            prep = f"{self.prepare_str} order by {','.join(self.sort_str)}"
        else:
            prep = self.prepare_str
        super().prepare(prep)
        for prm in self.param_str:
            super().addBindValue(prm)
        ret = super().exec()
        if Const.TEST_MODE:
            self.flog.to_log(f"""SQL exec {super().lastQuery()}""")
            if  ret:
                self.flog.to_log(f"""Params: {self.param_str}\nResult: Ok""")
            else:
                self.flog.to_log(f"""Params: {self.param_str}\nResult: WRONG!!!""")
        return ret


class QUsers(TSqlQuery):
        prepare_str = """select u.id, trim(u.name) as 'Фамилия И.О.', u.fam as 'Фамилия', u.ima as 'Имя', 
                u.otch as 'Отчество', u.login as 'Логин', u.phone as 'Телефон', 
                u.email as 'E-mail', u.birthday as 'Д.рожд', u.sertificate as 'Сертификат ПФДО',
                r.name as 'Роль', p.name as 'Место учёбы/работы', p.comment as 'Класс/Должн.',
                u.comment as 'Доп.информация'
               from users u
               join roles r on u.idRoles = r.id
               join places p on u.idPlaces = p.id
               join priv pp on pp.id = r.idPriv
               where pp.access like ?
        """

class QGroups(TSqlQuery):
    def __init__(self, *args, **kwargs):
        super(QGroups, self).__init__(*args, **kwargs)
        self.prepare_str = """select u.id, trim(u.name) as 'Фамилия И.О.', u.fam as 'Фамилия', u.ima as 'Имя', 
        """


if __name__ == '__main__':
    conn_str = 'Driver=SQL Server;Server=172.16.1.12,1433;Database=Journal4303;UID=sa;PWD=Prestige2011!;'
    app = QApplication(sys.argv)
    db =  QtSql.QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(conn_str)
    if db.open():
        if Const.TEST_MODE:
            print('Connect: Ok')

        usr = QUsers(params=(Const.ACC_PREPOD,))
        usr.refresh_select()
        usr.first()
        print(usr.value(1))