import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

'''Verbinden van pymongo en psycopg2 met python'''
postgresConnection = psycopg2.connect(user = "postgres",
                                  password = "groep5",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "voordeelshop")
postgresConnection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
cursor = postgresConnection.cursor();

'''' creeeren van database'''
def maak_database():
    cursor = con.cursor();
    name_database = 'Voordeelshop';
    sqlCreateDatabase = "create database "+name_database+";"
    cursor.execute(sqlCreateDatabase)


def maak_tabel():
    name_table = 'Products'
    sqlCreateTable = "create table " +name_table+ " ();"
    cursor.execute(sqlCreateTable)
    postgresConnection.commit()

maak_tabel()