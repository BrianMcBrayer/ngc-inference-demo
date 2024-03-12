from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        diagramDescription = request.form["diagramDescription"]

        # do inference here

        return render_template(
            "index.html",
            diagramDescription=diagramDescription,
            inferredDiagramText=diagramDescription,
        )

    return render_template("index.html")
