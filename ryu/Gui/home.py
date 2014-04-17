from bottle import route, run, request, abort, debug
import bottle_mysql

app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser='testuser', dbpass='test123', dbname='attackdb')
app.install(plugin)


@route('/attacks', method='GET')
def topics_list():
    print "list all attacks caught"
    db.execute('SELECT * from attacks')
    result = db.fetchall()
    
    return template('list_attacks', rows=result)

debug(True)
run(host='localhost', port=80, reloader=True)
