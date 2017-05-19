from flask import Flask
from Route import *
import sys
app=Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=int(sys.argv[1]))