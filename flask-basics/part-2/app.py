from flask import Flask, render_template  # render_template lets us serve HTML files

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # Flask looks in 'templates/' folder for this file


@app.route('/about')
def about():
    return render_template('about.html')  # Renders templates/about.html

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

