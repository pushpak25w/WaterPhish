from flask import Flask,render_template,url_for,request,redirect 
from features import phishing

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
	if request.method == "POST":
		url = request.form.get('url')
		val=int(phishing(url))
		if val==1:
			return 'not phishing'
		elif val==0:
			return 'suspicious'
		else:
			return 'phishing'

	return render_template('searchpage.html')