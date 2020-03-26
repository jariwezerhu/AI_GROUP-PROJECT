import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

'''Verbinden van pymongo en psycopg2 met python'''
postgresConnection = psycopg2.connect(user = "postgres",
                                  password = "ovk44yp6",
                                  host = "127.0.0.1",
                                  port = "5432",)
                                  # database = "voordeelshop")
postgresConnection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
cursor = postgresConnection.cursor();

''' creeeren van database'''
def maak_database():
    name_database = 'Voordeelshop';
    sqlDropDatabase = "DROP DATABASE IF EXISTS "+name_database+";"
    sqlCreateDatabase = "CREATE DATABASE "+name_database+";"
    cursor.execute(sqlDropDatabase)
    cursor.execute(sqlCreateDatabase)
    cursor.close

def maak_tabel():
    tabellen = ["products", "brand", "category", "Sub_category", "Sub_sub_category", "sessions", "orders", "profiles"]
    for i in tabellen:
        dropTabel = "DROP TABLE IF EXISTS {}".format(i)
        createTabel = "CREATE TABLE {}".format(i)
        cursor.execute(dropTabel)
        cursor.execute(createTabel)
    postgresConnection.commit()
    cursor.close()

maak_database()
maak_tabel()