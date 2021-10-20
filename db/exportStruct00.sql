--
-- Файл сгенерирован с помощью SQLiteStudio v3.2.1 в Вт окт 19 09:11:11 2021
--
-- Использованная кодировка текста: UTF-8
--

BEGIN TRANSACTION;

-- Таблица: courses
CREATE TABLE courses (
    id      INT       PRIMARY KEY,
    name    CHAR (100),
    volume  INT       DEFAULT (0),
    lesson  INT       DEFAULT (0),
    url     VARCHAR (200),
    year    INT       DEFAULT (2021),
    Target  CHAR (20),
    comment CHAR (100)    DEFAULT (''),
    acchour INT    DEFAULT (45),
    hday    INT    DEFAULT (2) 
);


-- Таблица: days
CREATE TABLE days (
    id    INT  PRIMARY KEY,
    name  CHAR,
    cname CHAR (5) 
);


-- Таблица: kabs
CREATE TABLE kabs (
    id    INT   PRIMARY KEY,
    name  CHAR (4),
    color CHAR (20) NOT NULL
                    DEFAULT '[(255, 255, 255)]'
);


-- Таблица: log
CREATE TABLE log (
    id   INT    PRIMARY KEY,
    name CHAR (100),
    date CHAR (20),
    time CHAR (20),
    info CHAR (200),
    uid  CHAR (10) 
);


-- Таблица: monts
CREATE TABLE monts (
    id   INT   PRIMARY KEY,
    num  INT,
    name CHAR (20) 
);


-- Таблица: places
CREATE TABLE places (
    id      INT    PRIMARY KEY,
    name    CHAR (200),
    comment CHAR (20)  DEFAULT ('') 
);


-- Таблица: priv
CREATE TABLE priv (
    id      INT    PRIMARY KEY,
    name    CHAR (40),
    access  CHAR (10),
    comment CHAR (100) DEFAULT ('') 
);


-- Таблица: rasp
CREATE TABLE rasp (
    id       INT    PRIMARY KEY,
    idGroups INT    NOT NULL,
    idKabs   INT    NOT NULL,
    start    CHAR (5),
    tend    CHAR (5),
    comment  CHAR (100),
    name     CHAR (100),
    idDays   INT    NOT NULL
                        DEFAULT (0) 
);


-- Таблица: roles
CREATE TABLE roles (
    id      INT    PRIMARY KEY,
    name    CHAR (200),
    idPriv  INT,
    FOREIGN KEY (idPriv) REFERENCES priv (id),
    comment CHAR (100) DEFAULT ('') 
);


-- Таблица: times
CREATE TABLE times (
    id   INT  PRIMARY KEY,
    name CHAR (6) 
);


-- Таблица: users
CREATE TABLE users (
    id          INT    PRIMARY KEY,
   fam         CHAR (40),
    ima         CHAR (40),
    otch        CHAR (40),
    phone       CHAR (11),
    email       CHAR (40),
    birthday    DATE,
    comment     CHAR (200) DEFAULT (''),
    idRoles     INT,
    FOREIGN KEY (idRoles) REFERENCES roles (id),
    idPlaces    INT,
    FOREIGN KEY (idPlaces) REFERENCES places (id),
    name        CHAR (50),
    passwd      BINARY (400),
    login       CHAR (30),
    sertificate CHAR (20)
);

-- Таблица: access
CREATE TABLE access (
    id       INT    PRIMARY KEY ,
    idUser   INT,
    FOREIGN KEY (idUser) REFERENCES users (id),
    datetime DATETIME,
    sel CHAR (300),
    idRole INT,
    FOREIGN KEY (idRole) REFERENCES roles (id)
);



-- Таблица: groups
CREATE TABLE groups (
    id        INT    PRIMARY KEY,
    name      CHAR (30),
    idUsers   INT,
    FOREIGN KEY (idUsers) REFERENCES users (id),
    idCourses INT,
    FOREIGN KEY (idCourses) REFERENCES courses (id) ON DELETE CASCADE
                                                 ON UPDATE NO ACTION,
    comment   CHAR (100) DEFAULT ('') 
);

-- Таблица: group_table
CREATE TABLE group_table (
    id       INT    PRIMARY KEY,
    idGroups INT,
    FOREIGN KEY (idGroups) REFERENCES groups (id),
    idUsers  INT,
    FOREIGN KEY (idUsers) REFERENCES users (id),
    comment  CHAR (200) DEFAULT ('') 
);




-- Таблица: journals
CREATE TABLE journals (
    id       INT     PRIMARY KEY,
    idGroups INT,
    FOREIGN KEY (idGroups) REFERENCES groups (id),
    date     DATETIME,
    start    CHAR (5),
    tend    CHAR (5),
    name     CHAR (100),
    present  CHAR (2048),
    estim    CHAR (2048),
    shtraf   CHAR (2048),
    comment  CHAR (100) 
);




-- Индекс: users_name
CREATE UNIQUE INDEX users_name ON users (
    name
);


-- Триггер: courses_in_groups
CREATE TRIGGER courses_in_groups ON courses
	AFTER DELETE
	AS
	IF EXISTS (SELECT 1 
      FROM groups
      WHERE idCourses = (select id from DELETED))
	BEGIN
    	RAISERROR ('groups data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: groups_in_group_table
CREATE TRIGGER groups_in_group_table ON groups
	AFTER DELETE
	AS         
	IF EXISTS (SELECT 1 
                     FROM group_table
                    WHERE idGroups = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('group_table data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;

-- Триггер: groups_in_journal
CREATE TRIGGER groups_in_journal ON groups
        AFTER DELETE
        AS
IF EXISTS (SELECT 1 
                     FROM journals
                    WHERE idGroups = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('journals data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: groups_in_rasp
CREATE TRIGGER groups_in_rasp ON groups
        AFTER DELETE
        AS
IF EXISTS (SELECT 1 
                     FROM rasp
                    WHERE idGroups = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('rasp data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: places_in_users
CREATE TRIGGER places_in_users ON places
AFTER DELETE
AS
IF EXISTS (SELECT 1 
                     FROM users
                    WHERE idPlaces = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('users data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: priv_in_roles
CREATE TRIGGER priv_in_roles ON priv
AFTER DELETE
AS
IF EXISTS (SELECT 1 
                     FROM roles
                    WHERE idPriv = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('roles data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: roles_in_users
CREATE TRIGGER roles_in_users ON roles
 AFTER DELETE
AS
IF EXISTS ( SELECT 1 
                     FROM users
                    WHERE idRoles = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('users data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: users_in_group
CREATE TRIGGER users_in_group ON users
 AFTER DELETE
AS
IF EXISTS ( SELECT 1
                     FROM groups
                    WHERE idUsers = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('group data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: users_in_group_table
CREATE TRIGGER users_in_group_table  ON users
  AFTER DELETE
AS
IF EXISTS (SELECT 1 
                     FROM group_table
                    WHERE idUsers = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('group_table data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;


-- Триггер: users_in_journals
CREATE TRIGGER users_in_journals ON users
 AFTER DELETE
AS
IF EXISTS ( SELECT 1 
                     FROM journals j 
                     join group_table gt on j.idGroups = gt.idGroups 
                    WHERE gt.idUsers = (select id from DELETED)
               )
	BEGIN
    	RAISERROR ('journals data used', 10, 1);
		ROLLBACK TRANSACTION;  
		RETURN   
	END;

COMMIT TRANSACTION;

