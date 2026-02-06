from flask import Flask, request, render_template_string
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
    overflow: hidden;
}
.card {
    background: white;
    width: 90%;
    max-width: 420px;
    padding: 28px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    animation: pop 0.5s ease;
}
@keyframes pop {
    from { transform: scale(0.85); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
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

.confetti {
    position: fixed;
    top: -10px;
    font-size: 22px;
    animation: fall 3s linear forwards;
}
@keyframes fall {
    to { transform: translateY(110vh) rotate(360deg); opacity: 0; }
}
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
    for (let i = 0; i < 80; i++) {
        let c = document.createElement("div");
        c.className = "confetti";
        c.innerHTML = "💖";
        c.style.left = Math.random() * 100 + "vw";
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 3000);
    }

    document.body.innerHTML = `
        <div class="card">
            <h2>💖 YES 💖</h2>
            <p>{{ yes_msg }}</p>
            <button class="share" onclick="share()">Share 💬</button>
        </div>
    `;
}

function share() {
    const text = encodeURIComponent("I just answered a Valentine proposal 💘");
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

    data = urllib.parse.quote(f"{sender}|{receiver}|{quote}")
    return f"""
    <div style='text-align:center'>
        <h3>Your Valentine link is ready 💘</h3>
        <a href='/v?d={data}'>Open Valentine</a>
    </div>
    """

@app.route("/v")
def valentine():
    sender, receiver, quote = urllib.parse.unquote(
        request.args.get("d")
    ).split("|")

    return render_template_string(
        HTML,
        page="proposal",
        sender=sender,
        receiver=receiver,
        yes_msg=quote
    )

if __name__ == "__main__":
    app.run()
