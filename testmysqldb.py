import MySQLdb
import sys

dsn_database = "id1153520_jsn_db"
dsn_host = "145.14.145.145"
dsn_port = 3306
dsn_uid = "id1153520_jsn_db"
dsn_pwd = "iot2014"


con = MySQLdb.connect(host=dsn_host, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
curs=con.cursor()


curs.execute("SELECT VERSION()")

data = curs.fetchone()

print "database version : %s " % data

con.close()
