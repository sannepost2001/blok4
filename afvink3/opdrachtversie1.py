# Sanne Post
# BIN-1A
# Zoek van organisme namen in Species.
import mysql.connector

conn = mysql.connector.connect(host="ensembldb.ensembl.org", user="anonymous", db="homo_sapiens_core_95_38")
cursor = conn.cursor()
zoekwoord = input("Waar wil je op zoeken: ")
cursor.execute("select description from gene where description like '%" + zoekwoord + "%'")
records = cursor.fetchall()  # lijst met al de namen die het zoekwoord in de naam hebben
for row in records:
    print(row[0])
cursor.close()
conn.close()
