import datetime
import sqlite3
import pyodbc
import sys
from datetime import datetime
from configparser import ConfigParser

from classes.cl_const import Const
from classes.qt__classes import LogWriter


class Sql:
    def __init__(self, database, srv_name, srv_port):
        self.server = f"{srv_name},{srv_port}"
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                   "Server="+self.server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))
    def get_connect(self):
        return self.cnxn


class ConnectDb:
    def __init__(self, path=None):
        flog = LogWriter()
        self.path = path
        self.con = None
        try:
            cfg = ConfigParser()
            if path:
                cfg.read(path, encoding='utf8')
            else:
                cfg.read('settings.ini')
            self.DB_name = cfg.get("Settings", "db_name")
            self.srv_name = cfg.get("Settings", "srv_name")
            self.srv_port = cfg.get("Settings", "srv_port")
            Const.YEAR = int(cfg.get("Settings", "l_year"))
            Const.D_START = cfg.get("Settings", "otch_start")
            Const.D_END = cfg.get("Settings", "otch_end")

        except FileNotFoundError:
            flog.to_log(f"""Не найден файл [settings.ini]""")
            sys.exit()
        except ConfigParser:
            flog.to_log(f"""Нарушена структура файла [settings.ini]""")
            sys.exit()

        try:
            flog.to_log(f""" Старт подключения БД: {self.srv_name}:{self.srv_port}/{self.DB_name}""")
            self.con = Sql(self.DB_name, self.srv_name, self.srv_port).get_connect()
            # self.con = sqlite3.connect(self.path)
            flog.to_log(f""" ----------------> Подключена БД: {self.srv_name}:{self.srv_port}/{self.DB_name}""")
            # print('Подключена БД:',  path)
        except Exception as err:
            flog.to_log(f"""СТОП!!! \n\t{err} \n\tПодключение не удалось {self.srv_name}:{self.srv_port}/{self.DB_name}""")
            sys.exit()

    def get_con(self):
        return self.con

if __name__ == '__main__':
    con = ConnectDb().get_con()
    print(con.autocommit)