from flask import Flask, request, redirect
import requests

app = Flask(__name__)

FB_APP_ID = "3956926761209187"  # Replace with your Facebook App ID
FB_APP_SECRET = "ee714dcc2c53a8d48717b842bfea9268"  # Replace with your Facebook App Secret
REDIRECT_URI = "http://localhost:5001/callback"  # Callback URL
SENSITIVE_DATA = {
    "email": "user@example.com",
    "files": ["file1.pdf", "file2.docx"],
    "account_balance": "$10,000"
}

@app.route('/')
def index():
    oauth_url = (
        f"https://www.facebook.com/v16.0/dialog/oauth?"
        f"client_id={FB_APP_ID}&redirect_uri={REDIRECT_URI}&scope=email"
    )
    return f'<a href="{oauth_url}">Login with Facebook</a>'

@app.route('/callback')
def callback():
    code = request.args.get("code")
    token_url = f"https://graph.facebook.com/v16.0/oauth/access_token"
    response = requests.get(token_url, params={
        "client_id": FB_APP_ID,
        "redirect_uri": REDIRECT_URI,
        "client_secret": FB_APP_SECRET,
        "code": code
    })
    
    access_token = response.json().get("access_token")
    
    if access_token:
        return f"Access Token: {access_token}<br>Sensitive Data: {SENSITIVE_DATA}"
    else:
        return "Failed to obtain access token."

if __name__ == '__main__':
    app.run(debug=True)
