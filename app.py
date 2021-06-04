from flask import Flask,render_template,url_for,request,redirect 
from features import phishing

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
	output = ""
	warnings = []
	if request.method == "POST":
		url = request.form.get('url')

		if(url==""):
			return render_template('searchpage.html')

		val, warnings = phishing(url)
		val = int(val)
		if val==1:
			output = "Legitimate"
		elif val==0:
			output = "Suspicious"
		else:
			output = "Phishing"

	return render_template('searchpage.html', output = output, warnings = warnings)

if __name__ == "__main__":
	app.run(debug=True)
