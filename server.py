from flask import Flask
from flask import render_template,request
import csv
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


def write_to_csv(data):
	with open('details.csv', 'a', newline='') as db:
		name = data["name"]
		email = data["email"]
		sub = data["subject"]
		msg = data["message"]
		spamwriter = csv.writer(db, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([name,email,sub,msg])  
        

@app.route('/contact', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return 'form submitted'





