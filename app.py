from flask import Flask

app = Flask("__main__")

@app.route("/")
def Greet():
    return "Hey Maccha"

if __name__ == "__main__":
    app.run(debug=True)