from flask import Flask, render_template, redirect, request, session, escape, Markup
from bokeh.plotting import figure
from bokeh.embed import components
app = Flask(__name__)
app.secret_key = "KeepItSecretKeepItSafe"
@app.route("/")
def input():
    return render_template("index.html")
@app.route("/plot", methods=["POST"])
def plot():
    session["x"] = [int(x) for x in request.form["xaxis"].split(",")]
    session["y"] = [int(x) for x in request.form["yaxis"].split(",")]
    return redirect("/success")
@app.route("/success")
def success():
    plot = figure(title=None, x_axis_label='x', y_axis_label='y')
    plot.line(session["x"], session["y"], legend=None, line_width=2)
    script, div = components(plot)
    return render_template("success.html", div=Markup(div), script=Markup(script))
app.run(debug=True)