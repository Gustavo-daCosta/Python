import sqlite3
from sqlite3 import Error
import os

pastaAPP = os.path.dirname(os.path.abspath(__file__))
nomeBanco = 'agenda/agenda.db'

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

# Data Query Language
def dql(query): # Select
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dml(query): # Insert, Update, Delete
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
