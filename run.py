from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def helloWorld():
	return render_template('getUserDetails.html')
	#return "Hello Everyone!"

if __name__ == '__main__':
	#host = os.getenv('IP','0.0.0.0')
	#port = int(os.getenv('PORT',5000))
	#app.debug = True;
	#app.run(host=host, port=port)
	app.run()
