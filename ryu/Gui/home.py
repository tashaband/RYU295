import bottle
from bottle import route, run, request, abort, debug, template , static_file
import MySQLdb as mdb


@route('/packets', method='GET')
@route('/', method='GET')
def attacks_list():
    print "list all received packets and their protocols"
    dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
    cursor = dbcon.cursor()
    cursor.execute("SELECT * FROM packets")
    result = cursor.fetchall()
    return template('packets', rows=result)

@route('/attacks', method='GET')
def attacks_list():
    print "list all attacks caught"
    dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
    cursor = dbcon.cursor()
    cursor.execute("SELECT * FROM attacks")
    result = cursor.fetchall()   
    return template('attacks', rows=result)

@route('/rules', method='GET')
def attacks_list():
    print "list all attacks rules"
    fname = '/home/ubuntu/RYU295/ryu/lib/ids/rules.txt'
    with open(fname) as f:
            rules = f.readlines()
    return template('rules', rows=rules)

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/<filename:re:.*\.png>')
def stylesheets(filename):
    return static_file(filename, root='static/img')

debug(True)
run(reloader=True)
