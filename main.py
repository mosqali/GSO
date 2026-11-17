from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template("Anmelden.html")

@app.route("/PasswortVergessen")
def passwortVergessen():
    return render_template("PasswortVergessen.html")

@app.route("/Registrierung")
def registrierung():
    return render_template("Registrierungs.html")

@app.route("/Verifizierung")
def verifizierung():
    return render_template("Verifizierungs.html")
@app.route("/Homepage")
def homepage():
    return render_template("HomepageBigScreen.html")

if __name__ == "__main__":
    app.run(debug=True)
