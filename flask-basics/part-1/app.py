from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Pratiksha!</h1>" "<p>Welcome to Flask</p>"

@app.route('/about')
def about():
    return "This is the about page"

if __name__ == '__main__':
    app.run(debug=True)
 
