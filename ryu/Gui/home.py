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
    fname = '/home/ubuntu/RYU/ryu/lib/ids/rules.txt'
    with open(fname) as f:
            rules = f.readlines()
    return template('rules', rows=rules)


@route('/editRules', method='GET')
def edit_rules():
    print "Edit attacks rules"
    fname = '/home/ubuntu/RYU/ryu/lib/ids/rules.txt'
    with open(fname) as f:
            rules = f.read()
    print rules
    return template('editRules', rows=rules)

@route('/rules', method='POST')
def change_rules():
    print "change attacks rules"
    post_rules = request.forms.get('rule_data')
    print "new rules : ", post_rules
    fname = '/home/ubuntu/RYU/ryu/lib/ids/rules.txt'
    open(fname,'w').close()
    f = open(fname, 'w')
    f.write(post_rules)
    f.close()

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
