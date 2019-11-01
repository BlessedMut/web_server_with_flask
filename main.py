from flask import Flask,render_template
from flask_autoindex import AutoIndex

app = Flask(__name__)

ppath = "/root/Desktop/programming/projects/Webserver/htdocs/"

app = Flask(__name__)
AutoIndex(app, browse_root=ppath) 

print(ppath)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/faq")
def faq():
	return render_template('faq.html')

@app.route("/inst")
def inst():
	return render_template('inst.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=83)
 