from flask import Flask, request, redirect, url_for, render_template_string
import uuid

app = Flask(__name__)

DATA = {}

HTML_HOME = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Valentine Generator 💘</title>
<style>
body{
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#ff758c,#ff7eb3);
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:0;
}
.card{
    background:#fff;
    padding:22px;
    border-radius:18px;
    width:92%;
    max-width:360px;
    text-align:center;
}
input,button{
    width:100%;
    padding:14px;
    margin-top:12px;
    border-radius:14px;
    border:1px solid #ddd;
    font-size:16px;
}
button{
    background:#ff4d6d;
    color:#fff;
    border:none;
}
</style>
</head>
<body>
<div class="card">
<h2>💘 Valentine Generator</h2>
<form method="post">
<input name="sender" placeholder="Your name" required>
<input name="receiver" placeholder="Your love's name" required>
<input name="quote" placeholder="Optional love quote">
<button>Create Link 💝</button>
</form>
</div>
</body>
</html>
"""

HTML_SHARE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Share 💌</title>
<style>
body{
    background:#ffdde1;
    font-family:Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    margin:0;
}
.card{
    background:#fff;
    padding:24px;
    border-radius:20px;
    width:92%;
    max-width:360px;
    text-align:center;
}
a{
    display:block;
    background:#25D366;
    color:white;
    padding:14px;
    border-radius:14px;
    text-decoration:none;
    margin-top:14px;
    font-size:18px;
}
</style>
</head>
<body>
<div class="card">
<h2>Link Created 💘</h2>
<p>Send this to {{ receiver }}</p>

<a href="https://wa.me/?text={{ msg }}">Share on WhatsApp 💬</a>
</div>
</body>
</html>
"""

HTML_PROPOSAL = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>💘 Proposal</title>
<style>
body{
    background:linear-gradient(135deg,#ff9a9e,#fad0c4);
    font-family:Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    margin:0;
}
.card{
    background:#fff;
    padding:24px;
    border-radius:20px;
    width:92%;
    max-width:360px;
    text-align:center;
}
button{
    padding:14px;
    width:45%;
    border-radius:14px;
    border:none;
    font-size:16px;
}
.yes{background:#38b000;color:#fff;}
.no{background:#d00000;color:#fff;}
</style>
<script>
function sayYes(){
    document.getElementById("result").innerHTML =
    "💖 {{ sender }} says:<br><br>{{ quote }}";
}
function sayNo(){
    document.getElementById("result").innerHTML =
    "😢 Better luck next time, {{ sender }}!";
}
</script>
</head>
<body>
<div class="card">
<h2>{{ receiver }}, will you be my Valentine? 💘</h2>

<div style="margin-top:20px;">
<button class="yes" onclick="sayYes()">YES 💖</button>
<button class="no" onclick="sayNo()">NO 😅</button>
</div>

<p id="result" style="margin-top:20px;font-size:18px;"></p>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        uid = str(uuid.uuid4())[:8]
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        quote = request.form.get("quote") or "I’ve liked you more than pizza ❤️"

        DATA[uid] = {
            "sender": sender,
            "receiver": receiver,
            "quote": quote
        }

        link = request.url_root + "p/" + uid
        msg = f"{sender} has a Valentine question for you 💘\\n\\nClick here 👉 {link}"
        return render_template_string(HTML_SHARE, receiver=receiver, msg=msg)

    return render_template_string(HTML_HOME)

@app.route("/p/<uid>")
def proposal(uid):
    d = DATA.get(uid)
    if not d:
        return "Link expired 😢"

    return render_template_string(
        HTML_PROPOSAL,
        sender=d["sender"],
        receiver=d["receiver"],
        quote=d["quote"]
    )

if __name__ == "__main__":
    app.run()
