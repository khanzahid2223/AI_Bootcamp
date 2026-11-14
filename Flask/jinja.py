# Building URL Dynamically
# Variable Rule
# Jinja2 Template Engine
"""
{{ }}-->Expression to print any output in HTML
{%....%}-->Conditonal Statements,Loops
{#...#}-->Comments
"""

##Intigration of HTML
from flask import Flask, render_template, request

# WSGI Application
app = Flask(__name__)

# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)

@app.route("/success_results/<int:score>")
def success_results(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)


if __name__ == "__main__":
    app.run(debug=True)
