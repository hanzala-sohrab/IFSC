import csv
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute("DROP TABLE api_ifsc;")
cur.execute(
    'CREATE TABLE "api_ifsc" ("ID"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,"BANK"	varchar(50) NOT NULL, "IFSC"	varchar(12) NOT NULL, "BRANCH" varchar(50) NOT NULL, "CENTRE"	varchar(50) NOT NULL, "DISTRICT"	varchar(50) NOT NULL, "STATE"	varchar(50) NOT NULL, "ADDRESS"	varchar(1000) NOT NULL, "CONTACT"	varchar(15) NOT NULL, "IMPS"	varchar(6), "RTGS"	varchar(6),	"CITY"	varchar(50) NOT NULL, "NEFT"	varchar(6),	"MICR"	varchar(18), "UPI"	varchar(6));')

with open('IFSC.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['BANK'].upper(), i['IFSC'].upper(), i['BRANCH'].upper(), i['CENTRE'].upper(), i['DISTRICT'].upper(), i['STATE'].upper(), i['ADDRESS'].upper(), i['CONTACT'].upper(),
              i['IMPS'].upper(), i['RTGS'].upper(), i['CITY'].upper(), i['NEFT'].upper(), i['MICR'].upper(), i['UPI'].upper()) for i in dr]

cur.executemany(
    "INSERT INTO api_ifsc('BANK', 'IFSC', 'BRANCH', 'CENTRE', 'DISTRICT', 'STATE', 'ADDRESS', 'CONTACT', 'IMPS', 'RTGS', 'CITY', 'NEFT', 'MICR', 'UPI') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
    to_db);
conn.commit()
conn.close()
