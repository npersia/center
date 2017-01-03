from bottle import route, default_app, template, run, static_file, error


@route('/')
def index():
    return template("./center/page/center.html")


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='0.0.0.0', port=8000)
