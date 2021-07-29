from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return f'<h1>About Page</h1>'

if __name__ == "__main__":
    app.run(debug=True)