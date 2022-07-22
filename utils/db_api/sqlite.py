import sqlite3
from datetime import datetime

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            username varchar(100),
            full_name varchar(100),
            phone varchar(15),
            address varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, username: str, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id) VALUES(1)"

        sql = """
        INSERT INTO Users(id, username, language) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, username, language), commit=True)
    
    def set_language(self, id, language):
        sql = f"""
        UPDATE Users SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(language, id), commit=True)
    
    def edit_user(self, id, full_name, phone, address):
        sql = f"""
        UPDATE Users SET full_name=?, phone=?, address=? WHERE id=?
        """
        return self.execute(sql, parameters=(full_name, phone, address, id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 "
        sql = f"SELECT * FROM Users WHERE id={id}"

        return self.execute(sql, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


    def create_table_messages(self):
        sql = """
        CREATE TABLE Messages (
            id int NOT NULL,
            User_id int references Users(id),
            message MEDIUMTEXT(1000),
            datetime datetime,
            replied BIT DEFAULT 0,
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    def add_message(self, id: int, user_id: str, text: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id) VALUES(1)"
        dtime = datetime.now()
        dtime = f"{dtime.year}-{dtime.month}-{dtime.day} {dtime.hour}:{dtime.minute}"

        sql = """
        INSERT INTO Messages(id, user_id, message, datetime) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, user_id, text, dtime), commit=True)

    def select_all_messages(self):
        sql = """
        SELECT * FROM Messages
        """
        return self.execute(sql, fetchall=True)

    def select_message(self, id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 "
        sql = f"SELECT User_id FROM Messages WHERE id={id}"

        return self.execute(sql, fetchone=True)
    
    def set_replied(self, id):
        sql = f"""
        UPDATE Messages SET replied=1 WHERE id={id}
        """
        return self.execute(sql, commit=True)

    def count_messages(self):
        return self.execute("SELECT COUNT(*) FROM Messages;", fetchone=True)

    def create_table_rules(self):
        sql = """
        CREATE TABLE Rules (
            id int NOT NULL,
            rules_uz MEDIUMTEXT(1000),
            rules_en MEDIUMTEXT(1000),
            rules_ru MEDIUMTEXT(1000),
            PRIMARY KEY (id)
            );

        """
        self.execute(sql, commit=True)

    def get_rules(self):
        sql = f"SELECT * FROM Rules WHERE id=1"
        return self.execute(sql, fetchone=True)

    def set_rules_uz(self, rules_uz: str):
        sql = f"""
        UPDATE Rules SET rules_uz=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_uz, 1), commit=True)

    def set_rules_en(self, rules_en):
        sql = f"""
        UPDATE Rules SET rules_en=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_en, 1), commit=True)
    
    def set_rules_ru(self, rules_ru):
        sql = f"""
        UPDATE Rules SET rules_ru=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_ru, 1), commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")