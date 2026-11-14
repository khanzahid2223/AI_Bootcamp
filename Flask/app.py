from flask import Flask

# WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome Zahid Bhai.How are you.How is your AI Journey"

@app.route("/index")
def index():
    return "This is index page"

if __name__ == "__main__":
    app.run(debug=True)
