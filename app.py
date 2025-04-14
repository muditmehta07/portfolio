from flask import Flask, render_template, request, url_for, redirect
import smtplib
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

        self.experience = {
            "1": {
                "Company": "Wipro Limited",
                "Title": "Project Intern",
                "From Date": "Jun 2024",
                "To Date": "Aug 2024",
                "Location": "Bengaluru, Karnataka",
                "Mode": "Hybrid",
                "Line 1": "Built AI-powered search tool using LangChain and Azure Cognitive Search to recommend proprietary software.",
                "Line 2": "Implemented vector embeddings to process queries and enhance search accuracy within the company's software ecosystem."
            },

            "2": {
                "Company": "HP (India Sales Pvt. Ltd.)",
                "Title": "Intern",
                "From Date": "Jun 2023",
                "To Date": "Aug 2023",
                "Location": "Gurugram, Haryana",
                "Mode": "On-Site",
                "Line 1": "Collaborated with the marketing team, identified need for AI-based retail tracking system.",
                "Line 2": "Partnered with AI companies to deploy AI-powered retail analytics tools."
            },

            "3": {
                "Company": "Swar Kala Sangam (Performing Arts Pvt. Ltd.)",
                "Title": "Web Developer",
                "From Date": "Nov 2021",
                "To Date": "Jul 2022",
                "Location": "Gurugram, Haryanaa",
                "Mode": "On-Site",
                "Line 1": "Handled and resolved backend queries to ensure seamless performance and functionality.",
                "Line 2": "Deployment, monitoring, and maintenance of the web application on Amazon Web Services (AWS)."
            },

            "4": {
                "Company": "Freelance",
                "Title": "Discord Bot Developer",
                "From Date": "Jun 2020",
                "To Date": "May 2021",
                "Location": "Gurugram, Haryana",
                "Mode": "Remote",
                "Line 1": "Developed custom Discord bots tailored to client needs using Python and the Discord.py framework.",
                "Line 2": "Built ML-powered bots using TensorFlow, Keras and NLTK, while Pillow was used for dynamic visual content."
            }
        }

        self.projects = {
            "1": {
                "Name": "Software Installation Agent",
                "Description": "Associated with Wipro Limited",
                "Created": "Aug 2024",
                "Technologies": "Python, LangChain, Flask, Azure Cognitive Services",
                "Line 1": "Developed a semantic search tool in Python using LangChain powered by Azure Cognitive Search and Vector Embeddings.",
                "Line 2": "The tool utilizes Flask and Postman to manage input query responses."
            },

            "2": {
                "GitHub": "https://github.com/muditmehta07/Michelle-Archived",
                "Name": "Michelle (Archived)",
                "Description": "Your All-in-One Discord Companion",
                "Created": "Dec 2021",
                "Technologies": "Discord.py",
                "Line 1": "Built a Discord bot with features like welcome messages, anonymous confessions, reaction roles, and mini-games.",
                "Line 2": "Added XP levels, leaderboards, a virtual store, moderation tools, and integrations like YouTube and Google Translate."
            }
        }

        self.education = {
            "1": {
                "Degree": "B.Tech Computer Science & Engineering",
                "University": "Amity University",
                "Graduation Year": "2026",
                "Location": "Jaipur, Rajasthan",
                "Line 1": "Minor Degree in Bioinformatics",
                "Line 2": "Started a Developer Club"
            },

            "2": {
                "Degree": "High School",
                "University": "GD Goenka Public School",
                "Graduation Year": "2021",
                "Location": "Gurugram, Haryana",
                "Line 1": "Major in Computer Science",
                "Line 2": "Minor in Painting"
            }
        }

        self.about = {
                "Name": "Mudit M",
                "Bio": "22-year-old, Pre-final year Computer Science Engineering Student from Delhi NCR.",
                "Links": {
                    "Resume": "url_for('static', filename='resume.pdf')",
                    "Linkedin": "https://www.linkedin.com/in/muditmehta07/",
                    "GitHub": "https://github.com/muditmehta07",
                    "Mail": "mailto:muditmehta@icloud.com"
                },
                "Skills": ['Python', 'LangChain', 'TensorFlow', 'Flask', 'Golang', 'Gin', 'Azure Cognitive Services']
        }

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
    EMAIL_ADDRESS = "muditmehta254@gmail.com"
    EMAIL_PASSWORD = "nmph rokb azua kqyn"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "muditmehta@icloud.com"
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)