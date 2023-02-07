from flask import Flask

app: Flask = Flask(__name__)

@app.route("/home")
def home() -> str:
    return """
    <a href="/endpoint">endpoint</a>
    """

@app.route("/endpoint")
def i_know() -> str:
    return f"""
    я <b>знала</b> что ты придешь
    """
    
if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )
