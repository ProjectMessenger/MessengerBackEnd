from . import routes

@routes.route("/")
def hello():
	return "Hello World!"