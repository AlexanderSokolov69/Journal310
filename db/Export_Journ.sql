--
-- Файл сгенерирован с помощью SQLiteStudio v3.2.1 в Ср окт 20 14:27:37 2021
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: journals
CREATE TABLE journals (
    id       INTEGER     PRIMARY KEY AUTOINCREMENT,
    idGroups INTEGER     REFERENCES groups (id) ON DELETE RESTRICT,
    date     DATETIME,
    tstart    CHAR (5),
    tend    CHAR (5),
    name     CHAR (100),
    present  CHAR (2048),
    estim    CHAR (2048),
    shtraf   CHAR (2048),
    comment  CHAR (100) 
);

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         38,
                         45,
                         '2021-10-02',
                         '12:30',
                         '14:00',
                         'Установочное занятие',
                         '511 512 509 510 513 515',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         39,
                         45,
                         '2021-10-04',
                         '08:00',
                         '09:30',
                         'Урок 1. Знакомство с языком Python',
                         '518 511 512 509 510 515 519',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         40,
                         45,
                         '2021-10-09',
                         '12:30',
                         '14:00',
                         'Урок 2. Переменные, типы данных',
                         '511 512 509 510 514 515 519',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         41,
                         45,
                         '2021-10-11',
                         '08:00',
                         '09:30',
                         'Урок 3. Переменные, типы данных',
                         '518 511 522 512 509 510 514 519',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         42,
                         45,
                         '2021-10-16',
                         '12:30',
                         '14:00',
                         'Урок 4. Линейные алгоритмы',
                         '522 512 509 514 519',
                         '',
                         '518=Киров 511=Болен 510=Киров 513=Соревн.',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         43,
                         45,
                         '2021-10-18',
                         '08:00',
                         '09:30',
                         'Урок 5. Линейные алгоритмы',
                         '518 522 512 509 510 513 514 519',
                         '',
                         '511=Болен',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         47,
                         1,
                         '2021-09-03',
                         '16:00',
                         '17:30',
                         'Установочное занятие',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         48,
                         1,
                         '2021-09-07',
                         '16:00',
                         '17:30',
                         'Повторение. Решение задач на основные конструкции данных',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         49,
                         1,
                         '2021-09-10',
                         '16:00',
                         '17:30',
                         'Пропуск.....',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         50,
                         1,
                         '2021-09-14',
                         '16:00',
                         '17:30',
                         'Повторение. Решение задач на классы',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         51,
                         1,
                         '2021-09-17',
                         '16:00',
                         '17:30',
                         'Повторение. Проектирование классов',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         52,
                         1,
                         '2021-09-21',
                         '16:00',
                         '17:30',
                         'QT 1. Что такое QT и PyQT. Знакомство',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         53,
                         1,
                         '2021-09-24',
                         '16:00',
                         '17:30',
                         'QT 2. QtDesigner, pyuic, два способа подключения uic-файла',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         54,
                         1,
                         '2021-09-28',
                         '16:00',
                         '17:30',
                         'Пропуск...',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         55,
                         1,
                         '2021-10-01',
                         '16:00',
                         '17:30',
                         'QT 3. Обработка исключений. Создание собственных исключений',
                         '164',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         56,
                         1,
                         '2021-10-05',
                         '16:00',
                         '17:30',
                         'QT 4. Файлы в Python. Типы файлов и работа с ними. Внутреннее устройство файлов',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         57,
                         1,
                         '2021-10-08',
                         '16:00',
                         '17:30',
                         'QT 5. Диалоги, работа с изображениями',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         58,
                         1,
                         '2021-10-12',
                         '16:00',
                         '17:30',
                         'QT. Установка дополнительных компонентов. PyQTGraph',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         59,
                         1,
                         '2021-10-15',
                         '16:00',
                         '17:30',
                         'Самостоятельная работа на файлы',
                         '164 165 166 167 168 169',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         60,
                         1,
                         '2021-10-19',
                         '16:00',
                         '17:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         61,
                         1,
                         '2021-10-22',
                         '16:00',
                         '17:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         62,
                         1,
                         '2021-10-26',
                         '16:00',
                         '17:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         63,
                         1,
                         '2021-10-29',
                         '16:00',
                         '17:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         72,
                         37,
                         '2021-09-04',
                         '13:15',
                         '14:45',
                         'Тема...',
                         '402 405 403 406 407 404 409 408 410 411 412',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         73,
                         37,
                         '2021-09-11',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         74,
                         37,
                         '2021-09-18',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         75,
                         37,
                         '2021-09-25',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         76,
                         37,
                         '2021-10-02',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         77,
                         37,
                         '2021-10-09',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         78,
                         37,
                         '2021-10-16',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         79,
                         37,
                         '2021-10-23',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         80,
                         37,
                         '2021-10-30',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         81,
                         37,
                         '2021-11-06',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         82,
                         37,
                         '2021-11-13',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         83,
                         37,
                         '2021-11-20',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         84,
                         37,
                         '2021-11-27',
                         '13:15',
                         '14:45',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         85,
                         38,
                         '2021-09-04',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '416 415 418 420 422 417 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         86,
                         38,
                         '2021-09-11',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '416 418 420 422 417 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         87,
                         38,
                         '2021-09-18',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '413 414 416 415 418 420 422 417 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         88,
                         38,
                         '2021-09-25',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '413 414 416 415 418 420 422 417 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         89,
                         38,
                         '2021-10-02',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '414 416 415 420 422 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         90,
                         38,
                         '2021-10-09',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '414 416 418 420 422 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         91,
                         38,
                         '2021-10-16',
                         '15:00',
                         '16:30',
                         'Тема...',
                         '413 414 416 415 418 420 422 417 419 423',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         92,
                         38,
                         '2021-10-23',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         93,
                         38,
                         '2021-10-30',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         94,
                         38,
                         '2021-11-06',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         95,
                         38,
                         '2021-11-13',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         96,
                         38,
                         '2021-11-20',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         97,
                         38,
                         '2021-11-27',
                         '15:00',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         98,
                         39,
                         '2021-09-04',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 426 428 520 430 431 432 519 433 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         99,
                         39,
                         '2021-09-11',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 428 520 430 431 519 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         100,
                         39,
                         '2021-09-18',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 426 428 430 431 519 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         101,
                         39,
                         '2021-09-25',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 427 428 520 430 431 519 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         102,
                         39,
                         '2021-10-02',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 428 520 430 431 519 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         103,
                         39,
                         '2021-10-09',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '426 428 520 430 431 432 433 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         104,
                         39,
                         '2021-10-16',
                         '16:40',
                         '18:10',
                         'Тема...',
                         '518 426 428 520 430 431 519 433 434 435',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         105,
                         39,
                         '2021-10-23',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         106,
                         39,
                         '2021-10-30',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         107,
                         39,
                         '2021-11-06',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         108,
                         39,
                         '2021-11-13',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         109,
                         39,
                         '2021-11-20',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         110,
                         39,
                         '2021-11-27',
                         '16:40',
                         '18:10',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         114,
                         45,
                         '2021-10-22',
                         '09:00',
                         '10:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         115,
                         45,
                         '2021-10-25',
                         '08:00',
                         '09:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         116,
                         45,
                         '2021-10-29',
                         '09:00',
                         '10:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         117,
                         11,
                         '2021-09-06',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         118,
                         11,
                         '2021-09-13',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         119,
                         11,
                         '2021-09-20',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         120,
                         11,
                         '2021-09-27',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         121,
                         19,
                         '2021-09-01',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         122,
                         19,
                         '2021-09-06',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         123,
                         19,
                         '2021-09-08',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         124,
                         19,
                         '2021-09-13',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         125,
                         19,
                         '2021-09-15',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         126,
                         19,
                         '2021-09-20',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         127,
                         19,
                         '2021-09-22',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         128,
                         19,
                         '2021-09-27',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         129,
                         19,
                         '2021-09-29',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         130,
                         18,
                         '2021-09-03',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         131,
                         18,
                         '2021-09-07',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         132,
                         18,
                         '2021-09-10',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         133,
                         18,
                         '2021-09-14',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         134,
                         18,
                         '2021-09-17',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         135,
                         18,
                         '2021-09-21',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         136,
                         18,
                         '2021-09-24',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         137,
                         18,
                         '2021-09-28',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         138,
                         20,
                         '2021-09-02',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         139,
                         20,
                         '2021-09-07',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         140,
                         20,
                         '2021-09-09',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         141,
                         20,
                         '2021-09-14',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         142,
                         20,
                         '2021-09-16',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         143,
                         20,
                         '2021-09-21',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         144,
                         20,
                         '2021-09-23',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         145,
                         20,
                         '2021-09-28',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         146,
                         20,
                         '2021-09-30',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         147,
                         13,
                         '2021-09-01',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         148,
                         13,
                         '2021-09-08',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         149,
                         13,
                         '2021-09-15',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         150,
                         13,
                         '2021-09-22',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         151,
                         13,
                         '2021-09-29',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         152,
                         15,
                         '2021-09-01',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         153,
                         15,
                         '2021-09-08',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         154,
                         15,
                         '2021-09-15',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         155,
                         15,
                         '2021-09-22',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         156,
                         15,
                         '2021-09-29',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         157,
                         10,
                         '2021-09-01',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         158,
                         10,
                         '2021-09-08',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         159,
                         10,
                         '2021-09-15',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         160,
                         10,
                         '2021-09-22',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         161,
                         10,
                         '2021-09-29',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         162,
                         6,
                         '2021-09-02',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         163,
                         6,
                         '2021-09-09',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         164,
                         6,
                         '2021-09-16',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         165,
                         6,
                         '2021-09-23',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         166,
                         6,
                         '2021-09-30',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         167,
                         17,
                         '2021-09-02',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         168,
                         17,
                         '2021-09-09',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         169,
                         17,
                         '2021-09-16',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         170,
                         17,
                         '2021-09-23',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         171,
                         17,
                         '2021-09-30',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         172,
                         8,
                         '2021-09-03',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         173,
                         8,
                         '2021-09-10',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         174,
                         8,
                         '2021-09-17',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         175,
                         8,
                         '2021-09-24',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         176,
                         6,
                         '2021-10-07',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         177,
                         6,
                         '2021-10-14',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         178,
                         6,
                         '2021-10-21',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         179,
                         6,
                         '2021-10-28',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         180,
                         8,
                         '2021-10-01',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         181,
                         8,
                         '2021-10-08',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         182,
                         8,
                         '2021-10-15',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         183,
                         8,
                         '2021-10-22',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         184,
                         8,
                         '2021-10-29',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         185,
                         10,
                         '2021-10-06',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         186,
                         10,
                         '2021-10-13',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         187,
                         10,
                         '2021-10-20',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         188,
                         10,
                         '2021-10-27',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         189,
                         11,
                         '2021-10-04',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         190,
                         11,
                         '2021-10-11',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         191,
                         11,
                         '2021-10-18',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         192,
                         11,
                         '2021-10-25',
                         '10:00',
                         '11:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         193,
                         13,
                         '2021-10-06',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         194,
                         13,
                         '2021-10-13',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         195,
                         13,
                         '2021-10-20',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         196,
                         13,
                         '2021-10-27',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         197,
                         15,
                         '2021-10-06',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         198,
                         15,
                         '2021-10-13',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         199,
                         15,
                         '2021-10-20',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         200,
                         15,
                         '2021-10-27',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         201,
                         17,
                         '2021-10-07',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         202,
                         17,
                         '2021-10-14',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         203,
                         17,
                         '2021-10-21',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         204,
                         17,
                         '2021-10-28',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         205,
                         18,
                         '2021-10-01',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         206,
                         18,
                         '2021-10-05',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         207,
                         18,
                         '2021-10-08',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         208,
                         18,
                         '2021-10-12',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         209,
                         18,
                         '2021-10-15',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         210,
                         18,
                         '2021-10-19',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         211,
                         18,
                         '2021-10-22',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         212,
                         18,
                         '2021-10-26',
                         '10:00',
                         '11:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         213,
                         18,
                         '2021-10-29',
                         '08:50',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         214,
                         19,
                         '2021-10-04',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         215,
                         19,
                         '2021-10-06',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         216,
                         19,
                         '2021-10-11',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         217,
                         19,
                         '2021-10-13',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         218,
                         19,
                         '2021-10-18',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         219,
                         19,
                         '2021-10-20',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         220,
                         19,
                         '2021-10-25',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         221,
                         19,
                         '2021-10-27',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         222,
                         20,
                         '2021-10-05',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         223,
                         20,
                         '2021-10-07',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         224,
                         20,
                         '2021-10-12',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         225,
                         20,
                         '2021-10-14',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         226,
                         20,
                         '2021-10-19',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         227,
                         20,
                         '2021-10-21',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         228,
                         20,
                         '2021-10-26',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         229,
                         20,
                         '2021-10-28',
                         '13:30',
                         '15:00',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         230,
                         12,
                         '2021-10-06',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         231,
                         12,
                         '2021-10-13',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         232,
                         12,
                         '2021-10-20',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         233,
                         12,
                         '2021-10-27',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         234,
                         14,
                         '2021-10-06',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         235,
                         14,
                         '2021-10-13',
                         '10:50',
                         '11:50',
                         'Тема: Клин',
                         '37 40 41 45 48 51',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         236,
                         14,
                         '2021-10-20',
                         '10:50',
                         '11:50',
                         'Тема: Винт',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         237,
                         14,
                         '2021-10-27',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         238,
                         9,
                         '2021-10-06',
                         '15:30',
                         '16:30',
                         'Тема: Наклонная плоскость',
                         '143 145 146 150 154 157 158 161 162',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         239,
                         9,
                         '2021-10-13',
                         '15:30',
                         '16:30',
                         'Тема: Клин',
                         '143 145 146 154 156 157 158 162',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         240,
                         9,
                         '2021-10-20',
                         '15:30',
                         '16:30',
                         'Тема: Винт',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         241,
                         9,
                         '2021-10-27',
                         '15:30',
                         '16:30',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         242,
                         5,
                         '2021-10-07',
                         '09:20',
                         '10:20',
                         'Тема: Наклонная плоскость',
                         '70 74 77 78 79 81 82 83 85 86 88',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         243,
                         5,
                         '2021-10-14',
                         '09:20',
                         '10:20',
                         'Тема: Клин',
                         '70 77 79 81 82 83 85 86 88',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         244,
                         5,
                         '2021-10-21',
                         '09:20',
                         '10:20',
                         'Тема: Винт',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         245,
                         5,
                         '2021-10-28',
                         '09:20',
                         '10:20',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         248,
                         16,
                         '2021-10-21',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         249,
                         16,
                         '2021-10-28',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         250,
                         7,
                         '2021-10-01',
                         '10:50',
                         '11:50',
                         'Тема: Блоки. Ременная передача',
                         '92 93 96 97 99 106 112 113 115',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         251,
                         7,
                         '2021-10-08',
                         '10:50',
                         '11:50',
                         'Тема: Наклонная плоскость',
                         '93 96 97 99 106 107 112 114',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         252,
                         7,
                         '2021-10-15',
                         '10:50',
                         '11:50',
                         'Тема: Клин',
                         '92 93 96 97 106 107 112 114 115',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         253,
                         7,
                         '2021-10-22',
                         '10:50',
                         '11:50',
                         'Тема: Винт',
                         '',
                         '',
                         '',
                         NULL
                     );

INSERT INTO journals (
                         id,
                         idGroups,
                         date,
                         tstart,
                         tend,
                         name,
                         present,
                         estim,
                         shtraf,
                         comment
                     )
                     VALUES (
                         254,
                         7,
                         '2021-10-29',
                         '10:50',
                         '11:50',
                         'Тема...',
                         NULL,
                         NULL,
                         NULL,
                         NULL
                     );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
