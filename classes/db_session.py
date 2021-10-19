import datetime
import sqlite3
import pyodbc
import sys
from datetime import datetime
from configparser import ConfigParser

from classes.cl_const import Const
from classes.qt__classes import LogWriter


class Sql:
    def __init__(self, database, server="SRV003-CUBE4303,1433"):
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                   "Server="+server+";"
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
                cfg.read(path)
            else:
                cfg.read('../settings.ini')
            self.path = cfg.get("Settings", "db_path")
            Const.YEAR = int(cfg.get("Settings", "l_year"))
            Const.D_START = cfg.get("Settings", "otch_start")
            Const.D_END = cfg.get("Settings", "otch_end")
            print(Const.D_START)
        except:
            flog.to_log(f"""Не найден файл [settings.ini]""")
            # print('settings.ini where?')
        try:
            self.con = Sql('Journal4303').get_connect()
            # self.con = sqlite3.connect(self.path)
            flog.to_log(f""" ----------------> Подключена БД: {self.path}""")
            # print('Подключена БД:',  path)
        except (sqlite3.Error, sqlite3.Warning) as err:
            flog.to_log(f"""СТОП!!! \n\t{err} \n\t{self.path}""")
            sys.exit()

    def get_con(self):
        return self.con

if __name__ == '__main__':
    print(ConnectDb().get_con())
