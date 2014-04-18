import bottle
from bottle import route, run, request, abort, debug, template
import MySQLdb as mdb



@route('/attacks', method='GET')
def attacks_list():
    print "list all attacks caught"
    dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
    cursor = dbcon.cursor()
  
    cursor.execute("SELECT * FROM attacks")
    result = cursor.fetchall()
    
    return template('attacks', rows=result)

debug(True)
run(reloader=True)
