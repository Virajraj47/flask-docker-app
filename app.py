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

      <h2>Pay via GPay</h2>

      <a href="upi://pay?pa=virajrajput610@okicici&pn=viraj&am=50&cu=INR">
        <button style="padding:10px 20px; font-size:16px; background:black; color:white; border-radius:5px;">
          Pay with GPay
        </button>
      </a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)