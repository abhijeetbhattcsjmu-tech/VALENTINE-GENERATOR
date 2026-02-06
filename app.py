from flask import Flask, request, render_template_string, url_for
import urllib.parse

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Valentine 💘</title>

<style>
body {
    margin: 0;
    min-height: 100vh;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    display: flex;
    align-items: center;
    justify-content: center;
}
.card {
    background: white;
    width: 90%;
    max-width: 420px;
    padding: 28px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
}
input, button {
    width: 100%;
    padding: 14px;
    margin-top: 12px;
    border-radius: 14px;
    border: none;
    font-size: 16px;
}
button { cursor: pointer; }
.yes { background: #2ec4b6; color: white; }
.no { background: #adb5bd; color: white; position: absolute; }
.share { background: #25D366; color: white; }
</style>
</head>

<body>

{% if page == "generator" %}
<div class="card">
    <h2>💘 Valentine Generator</h2>
    <form action="/create">
        <input name="sender" placeholder="Your name" required>
        <input name="receiver" placeholder="Their name" required>
        <input name="quote" placeholder="Custom YES quote (optional)">
        <button>Create Link 💖</button>
    </form>
</div>

{% elif page == "link" %}
<div class="card">
    <h3>🎉 Your Valentine Link</h3>
    <input value="{{ link }}" onclick="this.select()" readonly>
    <button class="share" onclick="share()">Share on WhatsApp 💬</button>
</div>

{% elif page == "proposal" %}
<div class="card" id="card">
    <h2>{{ sender }} 💌</h2>
    <p>{{ receiver }}, will you be my Valentine?</p>
    <button class="yes" onclick="yes()">YES 💘</button>
    <button class="no" id="no" onclick="move()">NO 😅</button>
</div>

<script>
function move() {
    const btn = document.getElementById("no");
    btn.style.left = Math.random() * (window.innerWidth - btn.offsetWidth) + "px";
    btn.style.top = Math.random() * (window.innerHeight - btn.offsetHeight) + "px";
}
function yes() {
    document.body.innerHTML = `
        <div class="card">
            <h2>💖 YES 💖</h2>
            <p>{{ yes_msg }}</p>
        </div>
    `;
}
function share() {
    const text = encodeURIComponent("Answer this Valentine proposal 💘 {{ link }}");
    window.open("https://wa.me/?text=" + text);
}
</script>
{% endif %}

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, page="generator")

@app.route("/create")
def create():
    sender = request.args.get("sender")
    receiver = request.args.get("receiver")
    quote = request.args.get("quote") or f"{receiver} accepted {sender}'s Valentine 💖"

    payload = urllib.parse.quote_plus(f"{sender}|{receiver}|{quote}")
    link = request.host_url.rstrip("/") + url_for("valentine") + "?d=" + payload

    return render_template_string(
        HTML,
        page="link",
        link=link
    )

@app.route("/v")
def valentine():
    data = urllib.parse.unquote_plus(request.args.get("d"))
    sender, receiver, quote = data.split("|")

    return render_template_string(
        HTML,
        page="proposal",
        sender=sender,
        receiver=receiver,
        yes_msg=quote
    )

if __name__ == "__main__":
    app.run()
