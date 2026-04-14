from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Sujeet ❤️ Sakshi</title>
      <style>
        body {
          background: linear-gradient(to right, #ff9a9e, #fad0c4);
          text-align: center;
          font-family: Arial, sans-serif;
          color: #fff;
          padding-top: 100px;
        }

        h1 {
          font-size: 50px;
          animation: glow 2s infinite alternate;
        }

        p {
          font-size: 22px;
          margin-top: 20px;
        }

        .heart {
          font-size: 60px;
          animation: beat 1s infinite;
        }

        button {
          margin-top: 30px;
          padding: 12px 25px;
          font-size: 18px;
          border: none;
          border-radius: 25px;
          background-color: #ff4b5c;
          color: white;
          cursor: pointer;
        }

        button:hover {
          background-color: #ff1e3c;
        }

        @keyframes beat {
          0% { transform: scale(1); }
          100% { transform: scale(1.2); }
        }

        @keyframes glow {
          from { text-shadow: 0 0 10px #fff; }
          to { text-shadow: 0 0 20px #ff4b5c; }
        }
      </style>
    </head>
    <body>

      <h1>Sujeet ❤️ Sakshi</h1>

      <div class="heart">💖</div>

      <p>
        You are the most beautiful part of my life 💕<br>
        Every moment with you feels magical ✨
      </p>

      <button onclick="showLove()">Click Me 💌</button>

      <p id="message"></p>

      <script>
        function showLove() {
          document.getElementById("message").innerText =
            "I Love You Sakshi ❤️ Forever Yours - Sujeet 💖";
        }
      </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)