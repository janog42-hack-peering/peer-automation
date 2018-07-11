from bottle import route, run,template

def getbgp():
    return("result")

@route('/')
def idx():
    return template('index', active="index")

@route('/manage')
def manage():
    return template('manage', active="manage")



run(host='localhost', port=8080, debug=True)