import bottle
from bottle import route, run, request, abort, debug, template , static_file
import MySQLdb as mdb



@route('/attacks', method='GET')
def attacks_list():
    print "list all attacks caught"
    dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
    cursor = dbcon.cursor()
  
    cursor.execute("SELECT * FROM attacks")
    result = cursor.fetchall()
    
    return template('attacks', rows=result)

@route('/packets', method='GET')
@route('/', method='GET')
def attacks_list():
    print "list all received packets and their protocols"
    dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
    cursor = dbcon.cursor()
  
    cursor.execute("SELECT * FROM packets")
    result = cursor.fetchall()
    
    return template('packets', rows=result)

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

debug(True)
run(reloader=True)
