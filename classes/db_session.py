import sqlite3
import sys
from configparser import ConfigParser

from classes.qt__classes import LogWriter


def connectdb(path=''):
    flog = LogWriter()
    try:
        cfg = ConfigParser()
        cfg.read("settings.ini")
        path = cfg.get("Settings", "db_path")
    except:
        flog.to_log(f"""Не найден файл [settings.ini]""")
        # print('settings.ini where?')
    try:
        con = sqlite3.connect(path)
        flog.to_log(f""" ----------------> Подключена БД: {path}""")
        # print('Подключена БД:',  path)
    except (sqlite3.Error, sqlite3.Warning) as err:
        flog.to_log(f"""СТОП!!! \n\t{err} \n\t{path}""")
        # print(err, path)
        sys.exit()
    return con

