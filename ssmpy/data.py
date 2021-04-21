import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file

    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def db_select_entry(conn, entry_list):
    """
    Query all rows in the entry table, where name is in entry_list
    :param conn: the Connection object
    :param entry_list: list of entity names

    :return: pandas dataframe with all columns in entry
    """

    placeholders = ', '.join(['"{}"'.format(value) for value in entry_list])

    query = '''SELECT * FROM entry WHERE name in ({});'''.format(placeholders)

    df = pd.read_sql_query(query, conn)

    return df


def db_select_entry_by_id(conn, entry_list):
    """
    Query all rows in the entry table, where name is in entry_list
    :param conn: the Connection object
    :param entry_list: list of entity ids

    :return: pandas dataframe with all columns in entry
    """

    placeholders = ', '.join(['"{}"'.format(value) for value in entry_list])

    query = '''SELECT * FROM entry WHERE id in ({});'''.format(placeholders)

    df = pd.read_sql_query(query, conn)

    return df


def db_select_transitive(conn, ids_list):
    """
    Query all rows in the transitive table, where id is in ids_list
    :param conn: the Connection object
    :param ids_list: list of entity ids

    :return: pandas dataframe with all columns in transitive
    """

    placeholders = ', '.join(['"{}"'.format(value) for value in ids_list])

    query = '''SELECT * FROM transitive WHERE entry1 in ({});'''.format(placeholders)

    df = pd.read_sql_query(query, conn)

    return df


def get_max_dest(conn):
    rows = conn.execute(
        """
        SELECT MAX(e.desc)
        FROM entry e
        """
    )
    maxfreq = rows.fetchone()[0] + 1.0

    return maxfreq
