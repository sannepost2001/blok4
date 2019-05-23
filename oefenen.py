# Maite van den Noort, bin-1a
# 22-05-2019
# applicatie om sql database te doorzoeken op een twee zoekwoorden,
# retoureneert ja of nee
import mysql.connector


def main():
    '''De main laat twee zoekwoorden invullen door de gebruiker, roept dan de
     twee functies zoeken en zoeken2. Die gaan met behulp van query zoeken in
      de database naar dat zoekwoord en stoppen het in records

    input: twee zoekwoorden
    output: '''
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org", user="anonymous",
        db='ensembl_production_95')
    zoekwoord1 = input('geef een zoekwoord op: ')
    zoekwoord2 = input('geef een tweede zoekwoord op:')
    records = zoeken(zoekwoord1)
    records2 = zoeken2(zoekwoord2)
    zelfde(records, records2)


def zoeken(zoekwoord1):
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org", user="anonymous",
        db='ensembl_production_95')
    cursor = conn.cursor()
    query1 = "select a.alias, s.common_name, s.scientific_name from species s join species_alias a on a.species_id = s.species_id where a.alias like '%" + zoekwoord1 + "%' or s.common_name like '%" + zoekwoord1 + "%' or s.scientific_name like '%" + zoekwoord1 + "%'"
    cursor.execute(query1)
    records = cursor.fetchall()
    cursor.close()
    print(records)
    return records


def zoeken2(zoekwoord2):
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org", user="anonymous",
        db='ensembl_production_95')
    cursor = conn.cursor()
    query2 = "select a.alias, s.common_name, s.scientific_name from species s join species_alias a on a.species_id = s.species_id where a.alias like '%" + zoekwoord2 + "%' or s.common_name like '%" + zoekwoord2 + "%' or s.scientific_name like '%" + zoekwoord2 + "%'"
    cursor.execute(query2)
    records2 = cursor.fetchall()
    cursor.close()
    print(records2)
    return records2


def zelfde(records, records2):
    org1 = []
    org2 = []
    org3 = []
    orga = []
    orgb = []
    orgc = []

    for row in records:
        org1 = row[0]
        org2 = row[1]
        org3 = row[2]
    for row in records2:
        orga = row[0]
        orgb = row[1]
        orgc = row[2]
    for row in records:
        if org1.find(orga) == 1:
            print('Het zijn gelijke organismen')
        elif org1 == orgb:
            print('Het zijn gelijke organismen')
        elif org1 == orgc:
            print('Het zijn gelijke organismen')
        elif org2 == orga:
            print('Het zijn gelijke organismen')
        elif org2 == orgb:
            print('Het zijn gelijke organismen')
        elif org2 == orgc:
            print('Het zijn gelijke organismen')
        elif org3 == orga:
            print('Het zijn gelijke organismen')
        elif org3 == orgb:
            print('Het zijn gelijke organismen')
        elif org3 == orgb:
            print('Het zijn gelijke organismen')
        else:
            print('het zijn niet gelijke organismen')


main()
