import sqlite3
import sys
import traceback as tb
import datetime

from classes.cl_const import Const
from classes.db_session import ConnectDb
from classes.qt__classes import LogWriter

from classes.t_tables import TUsers, TGroups, TRasp, TJournals, TGroupTable


def except_hook(cls, exception, traceback):
    global flog
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


class Statistics:
    def __init__(self, con, user_id=None):
        self.con = con
        self.user_id = user_id
        self.user = TUsers(self.con)
        self.groups = TGroups(self.con)
        self.rasp = TRasp(self.con)
        self.journ = TJournals(self.con)
        self.g_table = TGroupTable(self.con)
        self.update()

    def update(self):
        if self.user_id:
            self.user.set_filter(f"u.id={self.user_id}")
        else:
            self.user.set_filter('')
        if self.user_id:
            self.groups.set_filter(f"g.idUsers={self.user_id} and c.year={Const.YEAR}")
        else:
            self.groups.set_filter(f"c.year={Const.YEAR}")
            self.user.set_filter("u.id = (select gg.idUsers from groups gg where gg.idUsers = u.id)")
        if self.user_id:
            self.rasp.set_filter(f"g.idUsers = {self.user_id} and jc.year = {Const.YEAR}")
        else:
            self.rasp.set_filter(f"jc.year = {Const.YEAR}")
        if self.user_id:
            self.journ.set_filter(f"g.idUsers = {self.user_id} and jc.year = {Const.YEAR}")
        else:
            self.journ.set_filter(f"jc.year = {Const.YEAR}")
        if self.user_id:
            self.g_table.set_filter(f"g.idUsers = {self.user_id} and jc.year = {Const.YEAR}")
        else:
            self.g_table.set_filter(f"jc.year = {Const.YEAR}")

    def stat(self):
        ret = {'year': Const.YEAR,
               'id': self.user_id,
               'user': self.user.rows(),
               'groups': self.groups.rows(),
               'g_tables': self.g_table.rows(),
               'rasp': self.rasp.rows(),
               'journ': self.journ.rows()}
        dd_min = datetime.date.fromisoformat('2200-01-01')
        dd_max = datetime.date.fromisoformat('1900-01-01')
        for dd in self.journ.data:
            dd_min = min(datetime.date.fromisoformat(dd[Const.JRN_DATE]), dd_min)
            dd_max = max(datetime.date.fromisoformat(dd[Const.JRN_DATE]), dd_max)
        ret['date_min'] = dd_min
        ret['date_max'] = dd_max
        return ret

if __name__ == '__main__':
    flog = LogWriter(fname='teachLog.txt')
    sys.excepthook = except_hook
    con = ConnectDb().get_con()

    stat = Statistics(con)
    print(stat.stat())