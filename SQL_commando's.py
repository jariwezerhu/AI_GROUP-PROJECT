import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

'''Verbinden van pymongo en psycopg2 met python'''
con = psycopg2.connect("user=postgres password='groep5'");
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cursor = con.cursor();
name_database = 'Voordeelshop';
sqlCreateDatabase = "create database "+name_database+";"
cursor.execute(sqlCreateDatabase)