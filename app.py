from flask import Flask, render_template,redirect,request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template('index.html')


@app.route('/submit_form' , methods =['GET' , 'POST'] )
def submit():
    if request.method == 'POST':
        try:
            data =request.form.to_dict()
            write_data(data)
            message = 'SUBMITTED SUCCESSFULLY , WE WILL GET IN TOUCH WITH YOU SHORTLY :) !!'
            return render_template('thankyou.html', message=message)
        except:
            message = 'DID NOT SAVE TO DATABASE :('
            return render_template('thankyou.html' , message=message)
    else:
        message = 'FORM NOT SUBMITTED :('
        return render_template('thankyou.html' , message=message )


@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')
 
@app.route('/project1.html')
def prj():
    return render_template('project1.html')


@app.route('/project2.html')
def prj1():
    return render_template('project2.html')

def write_data(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

if __name__ =="__main__":
    app.run(debug=True)