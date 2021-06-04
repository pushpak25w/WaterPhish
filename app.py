from flask import Flask,render_template,url_for,request,redirect 
from features import phishing

app=Flask(__name__)


def phish():
	if request.method == "POST":
		url = request.form.get('url')

		val = phishing(url)
		val = int(val)

		if val==1:
			output = "Legitimate"
		elif val==0:
			output = "Suspicious"
		else:
			output = "Phishing!"

		return(output)

@app.route('/', methods=["GET","POST"])

def index():
	output = phish()
	return render_template('searchpage.html', output=output)

if __name__ == "__main__":
	app.run(debug=True)
