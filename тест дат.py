import datetime

from classes.bb_converts import date_us_ru, date_ru_us

def next_first_date(d: datetime):
    month = (d.month) % 12 + 1
    year = d.year + (month == 1)
    return datetime.date(year, month, 1)

def get_days_list(days: dict, mon=9, year=2021):
    d1 = datetime.date(year, mon, 1)
    d2 = next_first_date(d1)
    ret = []
    oneday = datetime.timedelta(1)
    print(d1)
    print(d2)
    while d1 < d2:
        if d1.weekday() in days.keys():
            ret.append([str(d1), *days[d1.weekday()]])
        d1 += oneday
    return ret


print(d.year, d.month, d.day, d.weekday())
# days = {0: ['08:00', '09:30'], 3: ['09:00', '10:30']}
# print(get_days_list(days))
