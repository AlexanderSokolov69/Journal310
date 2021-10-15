from classes.t__sqlobject import TSQLObject


class TRasp(TSQLObject):
    def set_sql(self, sql=None, ord='g.id'):
        self.keys = (
            ('idGroups', 'Учебная группа:'),
            ('idDays', 'День недели'),
            ('idKabs', 'Кабинет:'),
            ('start', 'Начало занятий:'),
            ('end', 'Окончание занятий:'),
            ('comment', 'Доп. информация')
        )
        self.dbname = 'rasp'
        if sql is None:
            self.sql = f"""select r.id, g.name || " - " || ju.name as "Группа - наставник", d.name as "День недели" , 
                    k.name as "Кабинет", r.start as "Начало", r.end as "Окончание", 
                    jc.acchour as "Акк. час", jc.hday as "Занятий в день", r.comment as "Доп. информация", 
                    r.idGroups as "Группа", d.id as "День"
                from rasp r
                join kabs k on r.idKabs = k.id
                join days d on r.idDays = d.id
                join groups g on r.idGroups = g.id
                join (select gu.id, u.name from groups gu join users u on gu.idUsers = u.id) ju on ju.id = g.id
                join (select cu.id, cu.acchour, cu.hday from courses cu) jc on jc.id = g.idCourses"""
            self.set_order('d.id, k.id, r.start')
        else:
            self.sql = f"""{sql}"""
            self.set_order(ord)


class TJournals(TSQLObject):
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
