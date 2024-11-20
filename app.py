from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/about-us")
def about_us():
    return render_template("about_us.html")


@app.route("/meat-and-potatoes")
def visualisation():
    return render_template("meat_and_potatoes.html")


if __name__ == '__main__':
    pass
