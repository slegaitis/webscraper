import os
import re
from flask import Flask, redirect, render_template, request, flash, url_for, session
from dotenv import load_dotenv

from scraper.webscraper import WebScraper

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route('/', methods=['GET'])
def home_route():
    session_data = dict(session)
    
    return render_template("index.html", web_scraper=session_data['web_scraper_result'] if 'web_scraper_result' in session_data else {}, address=session_data['address'] if 'address' in session_data else '')

@app.route('/form-submit', methods=['POST'])
def form_submit():
    form = dict(request.form)
    pattern = re.compile(r'^(http|HTTP)+(s|S)?:\/\/[\w.-]+(?:\.[\w\.-]+)+[\w\-\._\$\(\)/]+$')
    
    if 'address' in form and re.fullmatch(pattern, form['address']):
        scraper = WebScraper(url=form['address'])
        session['web_scraper_result'] = scraper.fetch()
        session['address'] = form['address']
        
        if len(session['web_scraper_result']['unique_tags']) == 0:
            flash(f"Entered an invalid address. Please check the address and try again.")
        
        return redirect(url_for('home_route'))
    else:
        flash(f"Entered an invalid address. Please check the address and try again.")
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)