import sqlite3


class Connect:
    con = sqlite3.connect("database/loginsystem.db")
