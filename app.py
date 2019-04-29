from flask import Flask, request, redirect, render_template
import operation2 as oo
app = Flask(__name__)

@app.route("/airpoll", methods= ['GET'])
def index():
	return render_template('index.html')

@app.route("/airpoll/result", methods = ['POST'])
def result():
	inp1 = request.form['inp1']
	inp2 = request.form['inp2']
	inp3 = request.form['inp3']
	inp4 = request.form['inp4']
	inp5 = request.form['inp5']
	inp6 = request.form['inp6']
	inp7 = request.form['inp7']
	inp8 = request.form['inp8']
	inp9 = request.form['inp9']
	name=[inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9]
	return render_template('result.html', name = oo.main(name))

if __name__ == "__main__":
	app.run(host='0.0.0.0')
