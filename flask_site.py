from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    output = text.upper()
    return render_template("home.html", value=output)

if __name__ == "__main__":
    app.run(debug=True)
