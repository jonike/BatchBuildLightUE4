from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import os
import sqlite3


class TableProgram(object):
    """Objects to work with the SQLite"""

    def __init__(self):
        super(TableProgram, self).__init__()
        self.base_sql = 'projects.db'
        self.bd_exist = os.path.exists(self.base_sql)

        self.bd = sqlite3.connect(self.base_sql)
        self.bd.cursor()

        if not self.bd_exist:
            self.create_data()

    def create_data(self):
        self.bd.execute('''CREATE TABLE  projects(
                id          INTEGER PRIMARY KEY,
                project_id  INT,
                paths_id    INT)''')

        self.bd.execute('''CREATE TABLE  paths(
                path_id     INTEGER PRIMARY KEY,
                editor      TEXT,
                project     TEXT)''')
        self.bd.execute('''CREATE TABLE levels(
                levels_id   INTEGER PRIMARY KEY,
                name        TEXT,
                path        TEXT)''')
        self.bd.commit()
        self.bd.close()

        msg_def = 'Create a news base data'
        print(msg_def)

    @staticmethod
    def read_data(table):
        msg_func = 'Read Data from the base data'
        print(msg_func)

    def write_data(self):
        self.bd.execute('''INSERT INTO paths VALUES (2, 'editor', 
        'project')''')

        self.bd.commit()

        msg_func = 'Write a news Data inside a table'
        print(msg_func)

