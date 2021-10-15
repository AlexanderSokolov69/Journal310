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
        self.dbname = 'journ'
        if sql is None:
            self.sql = f"""select r.id, g.name || " - " || ju.name as "Группа - наставник", d.name as "День недели" , 
                    k.name as "Кабинет", r.start as "Начало", r.end as "Окончание", 
                    jc.acchour as "Акк. час", jc.hday as "Занятий в день", r.comment as "Доп. информация", 
                    r.idGroups as "Группа", d.id as "День"
                from journ r
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


class TUsers(TSQLObject):
    def set_sql(self, sql=None, flt=None):
        self.keys = (
            ('name', 'Фамилия И.О.:'),
            ('fam', 'Фамилия:'),
            ('ima', 'Имя:'),
            ('otch', 'Отчество:'),
            ('login', 'Логин для входа в программу:'),
            ('phone', 'Номер телефона:'),
            ('email', 'e-mail адрес:'),
            ('birthday', 'Дата рождения:'),
            ('idRoles', 'Роль доступа:'),
            ('idPlaces', 'Место работы/учёбы:'),
            ('comment', 'Дополнительная информация:'),
            ('sertificate', 'Сертификат ПФДО:')
        )
        self.dbname = 'users'
        if sql is None:
            self.sql = f"""select u.id, u.name as 'Фамилия И.О.', u.fam as "Фамилия", u.ima as 'Имя', 
                u.otch as 'Отчество', u.login as 'Логин', u.phone as 'Телефон', 
                u.email as 'E-mail', u.birthday as 'Д.рожд', u.sertificate as 'Сертификат ПФДО',
                r.name as 'Роль', p.name as 'Место учёбы/работы', p.comment as 'Класс/Должн.',
                u.comment as 'Доп.информация'
               from users u
               join roles r on u.idRoles = r.id
               join places p on u.idPlaces = p.id"""
        else:
            self.sql = f"""{sql}"""


    def get_user_login(self, login):
        sql = f'select * from users where login = "{login.lower()}"'
        cur = self.con.cursor()
        data = cur.execute(sql).fetchone()
        if data:
            ret = {}
            for i, key in enumerate(cur.description):
                ret[key[0]] = data[i]
        else:
            ret = None
        return ret

    def set_user_password(self, id, passwd):
        sql = f"update users set passwd = ? where id = {id}"
        cur = self.con.cursor()
        cur.execute(sql, [passwd])
        self.con.commit()


class TGroups(TSQLObject):
    def set_sql(self, sql=None, ord='g.id'):
        self.keys = (
            ('name', 'Кодовое название учебной группы:'),
            ('idCourses', 'Учебная программа:'),
            ('idUsers', 'Фамилия И.О. наставника:')
        )
        self.dbname = 'groups'
        if sql is None:
            self.sql = f"""select g.id, g.name as "Группа", c.name as "Учебный курс", c.volume as "Объем", 
                    c.lesson as "Занятие", c.year as "Уч.год", u.name as "ФИО наставника" 
                from groups g
                join users u on g.idUsers = u.id
                join courses c on g.idCourses = c.id"""
        else:
            self.sql = f"""{sql}"""
        self.set_order(ord)


class TGroupTable(TSQLObject):
    def set_sql(self, sql=None, ord='u.name'):
        self.keys = (
            ('idGroups', 'Учебная группа:'),
            ('idUsers', 'Фамилия И.О. кубиста:'),
            ('comment', 'Дополнительная информация:')
        )
        self.dbname = 'group_table'
        if sql is None:
            self.sql = f"""select t.id as 'id', g.name as "Группа", u.name as "Фамилия И.О.", 
                    t.comment as "Комментарий" 
                from group_table t
                join groups g on g.id = t.idGroups
                join users u on u.id = t.idUsers"""
        else:
            self.sql = f"""{sql}"""
        self.set_order(ord)