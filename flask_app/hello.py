from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(name="World"):
    return "Hello " + name

# if __name__ == "__main__":
#     app.run(host="localhost", port="8080", debug=True)