from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>VirajCloud</title>
    </head>
    <body>
      <h1>Welcome to VirajCloud 🚀</h1>
      <p>Deployment successful via CI/CD</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)