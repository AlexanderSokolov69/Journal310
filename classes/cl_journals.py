from .cl__main_sqlobject import SQLObject


class Journals(SQLObject):
    def set_sql(self, sql=None, ord='j.date'):
        self.keys = (
            ('idGroups', 'Учебная группа:'),
            ('Date', 'Дата занятия'),
            ('name', 'Тема занятия:'),
            ('start', 'Начало занятий:'),
            ('end', 'Окончание занятий:'),
            ('present', 'Отметки о посещении'),
            ('estim', 'Отметки'),
            ('shtraf', 'Штрафы'),
            ('comment', 'Доп. информация')
        )
        self.dbname = 'journals'
        if sql is None:
            self.sql = f"""select j.id, j.date as "Дата", j.name as "Тема занятия", j.start as "Время нач.", 
                    j.end as "Время оконч.", j.comment as "Доп. информация"
                from journals j"""
            self.set_order('j.date, j.start')
        else:
            self.sql = f"""{sql}"""
            self.set_order(ord)
