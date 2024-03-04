from flask import Flask, render_template, request, jsonify
from app.scraper import scrape_data
from app.util import format_data
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Loadinf environment variables from .env file
load_dotenv()

# Access environment variables
app.config['EMAIL_ID'] = os.getenv('EMAIL_ID')
app.config['PASS_ID'] = os.getenv('PASS_ID')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    name = request.form['name']
    email = request.form['email']
    skills = request.form['skills']

    email_id = app.config['EMAIL_ID']
    pass_id = app.config['PASS_ID']

    print(email_id)

    #  # Perform web scraping
    # raw_data = scrape_data(name, email, skills)

    # Perform web scraping to get multiple job listings
    job_listings = scrape_data(email_id, pass_id, "https://cuvette.tech/app/student/jobs/internships/filters?sortByDate=true")

    # Format scraped data
    formatted_data = [format_data(job) for job in job_listings]

    # Format scraped data
    # formatted_data = format_data(raw_data)

    # Return formatted data as JSON response
    # return jsonify(raw_data)
    return render_template('index.html', job_listings=formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
