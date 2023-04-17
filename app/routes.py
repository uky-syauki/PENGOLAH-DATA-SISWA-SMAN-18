from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello Woy!"


@app.route("/user")
def user():
	return "This User"


@app.route("/daftar")
def daftar():
	return "This Daftar"