import sqlite3
import sys
from configparser import ConfigParser

from classes.cl_const import Const
from classes.qt__classes import LogWriter


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
        except:
            flog.to_log(f"""Не найден файл [settings.ini]""")
            # print('settings.ini where?')
        try:
            self.con = sqlite3.connect(self.path)
            flog.to_log(f""" ----------------> Подключена БД: {path}""")
            # print('Подключена БД:',  path)
        except (sqlite3.Error, sqlite3.Warning) as err:
            flog.to_log(f"""СТОП!!! \n\t{err} \n\t{path}""")
            sys.exit()

    def get_con(self):
        return self.con

if __name__ == '__main__':
    print(ConnectDb().get_con())