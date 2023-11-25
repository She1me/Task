from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello world!'

if __name__ == '__main__':
	app.run(debug=True, port=32777, host="0.0.0.0")
