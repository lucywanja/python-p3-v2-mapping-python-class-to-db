# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db') # CONN -A onstant equal to a hash that contains a connetion to a database
CURSOR = CONN.cursor()  # A constant that allows us to interact with the database and  execute SQL statements
