from flask import Flask,render_template,url_for,request,redirect 
from features import phishing

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
	if request.method == "POST":
		url = request.form.get('url')
		val=int(phishing(url))
		if val==1:
			print('not phishing')
		elif val==0:
			print('suspicious')
		else:
			print('phishing')

	return render_template('searchpage.html')

if __name__ == "__main__":
	app.run(debug=True)