from flask import Flask,render_template,url_for,request,redirect 
from features import phishing

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
	output = ""
	warnings = []
	if request.method == "POST":
		url = request.form.get('url')

		if(url=="" or url.count('.')==0):
			return render_template('searchpage.html',output="evu")

		val, warnings = phishing(url)
		val = int(val)
		if val==1:
			output = "Legitimate"
		elif val==0:
			output = "Suspicious"
		elif val==404:
			output="evu"
		else:
			output = "Phishing"
	return render_template('searchpage.html', output = output, warnings = warnings)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
	app.run(debug=True)
