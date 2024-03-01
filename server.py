from flask import Flask,render_template,url_for,request,redirect
import csv 

app = Flask(__name__)
print(__name__)

@app.route("/")
def initial():
    return render_template('index.html')

@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt','a') as f:
        f.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv',newline="",'a') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form",methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'