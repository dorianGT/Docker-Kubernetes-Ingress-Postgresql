from flask import Flask

app = Flask(__name__)

@app.route("/second")
def second_service_route():
    return "Hello from the Second Service!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
