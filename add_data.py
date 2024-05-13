import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def add_module(conn, module):
    """
    Create a new module into the modules table
    :param conn:
    :param module:
    :return: module id
    """
    sql = '''INSERT INTO modules(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, module)
    conn.commit()
    return cur.lastrowid


def add_submodule(conn, submodule):
    """
    Create a newsubmodule into the submodules table
    :param conn:
    :param submodule:
    :return: submodule id
    """
    sql = '''INSERT INTO submodules(module_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, submodule)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    module = ("Obiekty w Pythonie", "2020-05-13 00:00:00", "2020-05-20 00:00:00")

    conn = create_connection("database.db")
    mo_id = add_module(conn, module)

    submodule = (
        mo_id,
        "Metody w klasach",
        "Nauka tworzenia metod w klasach",
        "started",
        "2020-05-13 12:00:00",
        "2020-05-18 15:00:00"
    )

    submodule_id = add_submodule(conn, submodule)

    print(mo_id, submodule_id)
    conn.commit()
