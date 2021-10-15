import sqlite3
from sqlite3 import connect
from .qt__classes import LogWriter
from PyQt5.QtCore import pyqtSignal, QObject


class TSQLObject(QObject):
    need_to_refresh = pyqtSignal()

    def __init__(self, con: connect):
        """
        Базовый класс работы с БД SQL
        :param con: указатель на БД SQL
        """
        super(TSQLObject, self).__init__()
        if con is None:
            Exception('NO database connection')
        self.logfile = LogWriter()
        self.con: sqlite3.connect = con
        self.cur = con.cursor()
        self.sql = None
        self.filter = None
        self.order = None
        self.dbname = None
        self.header = []
        self.data = []
        self.keys = []
        self.set_filter()
        self.set_order()
        self.set_sql()
        self.update()

    def rows(self):
        """
        Количество записей в таблице
        :return:
        """
        if len(self.data[0]) == 0:
            return 0
        return len(self.data)

    def set_order(self, ord=None):
        """
        Сортировка для UPDATE
        :param ord:
        :return:
        """
        if ord:
            self.order = f"order by {ord}"
        else:
            self.order = ''

    def set_filter(self, flt=None):
        """
        Фильтр для UPDATE
        :param flt: строка для WHERE
        :return:
        """
        if flt:
            self.filter = f"where {flt}"
        else:
            self.filter = ''
        self.update()

    def set_sql(self, sql=None, flt=None):
        """
        Описание конкретной таблицы
        :param sql: SQL запрос для UPDATE
        :param flt: фильтр для UPDATE
        :return:
        """
        pass

    def update(self):
        """
        Обновление данных из БД SQL для визуализации
        :return:
        """
        if self.sql is not None:
            try:
                sql = f"""{self.sql} {self.filter} {self.order}"""
                ret = self.cur.execute(sql).fetchall()
                self.need_to_refresh.emit()
            except (sqlite3.Error, sqlite3.Warning) as err:
                self.logfile.to_log(f"""{err} [update class] \n{sql}""")
                ret = None
            if ret:
                self.header = [i[0] for i in self.cur.description]
                self.data = [['' if zp == None else zp for zp in rec] for rec in ret]
            else:
                self.data =[[]]
            return len(self.data)
        else:
            return 0

    # def update_model(self):
    #     """
    #     Обновление модели для визуальных виджетов
    #     :return:
    #     """
    #     self.rec_update(self.data[self.tmodel.current_index[0]][0],
    #                     {self.keys[self.tmodel.current_index[1] - 1][0]:
    #                          self.data[self.tmodel.current_index[0]][self.tmodel.current_index[1]]}
    #                     )
    #     self.need_to_save.emit()

    # def model(self):
    #     """
    #     Вернуть созданную модель
    #     :return:
    #     """
    #     return self.tmodel
    #
    def commit(self):
        """
        COMMIT изменений в БД
        :return:
        """
        try:
            self.con.commit()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [commit]""")

    def rollback(self):
        """
        ROLLBACK изменений в БД
        :return:
        """
        try:
            self.con.rollback()
            self.need_to_refresh.emit()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [rollback]""")

    def rec_update(self, id, arg: dict):
        """
        Обновление записи в БД
        :param id: ID записи
        :param arg: список кортежей для корректировки
        :return:
        """
        args = ', '.join([f'{item[0]} = "{item[1]}"' for item in arg.items()])
        sql = f"update {self.dbname} set {args} where id = {id}"
        try:
            self.cur.execute(sql)
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [update record] \n{sql}""")
        return True

    def rec_append(self, arg: dict):
        """
        Добавление записи в таблицу
        :param arg: словарь данных для записи в БД
        :return:
        """
        key = ', '.join(arg.keys())
        val = '"' + '", "'.join(arg.values()) +'"'
        sql = f"""insert into {self.dbname} ({key}) values ({val})"""
        try:
            self.cur.execute(sql)
            self.need_to_refresh.emit()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [append record] \n{sql}""")
        return True

    def rec_delete(self, id):
        """
        Удаление записи
        :param id: ID записи для удаления
        :return:
        """
        sql = f"delete from {self.dbname} where id = {id}"
        try:
            self.cur.execute(sql)
            self.need_to_refresh.emit()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [delete record] \n{sql}""")
        return True

    def get_record(self, id):
        """
        Получить запись таблицы по ID
        :param id: ID записи
        :return:
        """
        fields = ', '.join([key[0] for key in self.keys])
        sql = f"select {fields} from {self.dbname} where id = {id}"
        cur = self.con.cursor()
        data = None
        try:
            data = cur.execute(sql).fetchone()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [get record] \n{sql}""")
        if not data:
            data = [''] * len(self.keys)
        ret = []
        for i, key in enumerate(self.keys):
            key = list(key)
            key.append(data[i])
            ret.append(key)
        return ret

    def execute_command(self, comm):
        """
        Исполнение произвольной команды SQL
        :param comm: SQL команда
        :return:
        """
        cur = self.con.cursor()
        try:
            ret = cur.execute(comm).fetchall()
        except (sqlite3.Error, sqlite3.Warning) as err:
            self.logfile.to_log(f"""{err} [execute command] \n{comm}""")
            ret = [[]]
        return ret


if __name__ == '__main__':
    pass