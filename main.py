from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')