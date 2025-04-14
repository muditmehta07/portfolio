from flask import Flask, render_template, request, url_for, redirect
import smtplib
import json, settings
from email.message import EmailMessage

app = Flask(__name__, 
    static_url_path='',
    static_folder='static',
    template_folder='templates')

class Values:
    def __init__(self, page_title, page_percent):
        self.project_name = "Mudit's Portfolio"
        self.page_title = page_title
        self.page_percent = page_percent

        with open("./data/experience.json", "r") as f:
            self.experience = json.load(f)

        with open("./data/projects.json", "r") as f:
            self.projects = json.load(f)

        with open("./data/education.json", "r") as f:
            self.education = json.load(f)

        with open("./data/about.json", "r") as f:
            self.about = json.load(f)

@app.route('/')
def index():
    values = Values(page_title="Home", page_percent="13%")
    return render_template('index.html', values=values)

@app.route('/experience')
def experience():
    values = Values(page_title="Experience", page_percent="37%")
    return render_template('experience.html', values=values)

@app.route('/projects')
def projects():
    values = Values(page_title="Projects", page_percent="7%")
    return render_template('projects.html', values=values)

@app.route('/education')
def education():
    values = Values(page_title="Education", page_percent="83%")
    return render_template('education.html', values=values)

@app.route('/about')
def about():
    values = Values(page_title="About", page_percent="69%")
    success = request.args.get('success', False)
    return render_template('about.html', values=values, success=success)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    email_body = f"""
    Name: {name}
    Email: {email}
    Message: {message}
    """

    send_email("New Form Submission", email_body)
    return redirect(url_for('about', success=True))

def send_email(subject, body):
    EMAIL_ADDRESS = settings.EMAIL_FROM
    EMAIL_PASSWORD = settings.PASSWORD

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = settings.EMAIL_TO
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)