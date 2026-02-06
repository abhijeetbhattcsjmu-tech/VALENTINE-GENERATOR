from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Valentine 💘</title>

<style>
:root {
    --bg1: #ff758c;
    --bg2: #ff7eb3;
    --card: #ffffff;
    --text: #333;
}

.dark {
    --bg1: #1e1e2f;
    --bg2: #2a2a40;
    --card: #2f2f46;
    --text: #f1f1f1;
}

body {
    margin: 0;
    min-height: 100vh;
    background: linear-gradient(135deg, var(--bg1), var(--bg2));
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    color: var(--text);
    overflow: hidden;
}

.card {
    background: var(--card);
    width: 90%;
    max-width: 420px;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    text-align: center;
    z-index: 2;
}

button, input {
    width: 100%;
    padding: 14px;
    margin-top: 10px;
    border-radius: 14px;
    border: none;
    font-size: 16px;
}

button {
    cursor: pointer;
}

.generate { background: #ff3366; color: white; }
.yes { background: #2ec4b6; color: white; }
.no { background: #adb5bd; color: white; position: absolute; }
.share { background: #25D366; color: white; }
.darkbtn { background: #444; color: white; }

.heart {
    position: fixed;
    top: -10px;
    font-size: 20px;
    animation: fall 6s linear infinite;
    opacity: 0.7;
}

@keyframes fall {
    to { transform: translateY(110vh); }
}
</style>
</head>

<body class="{{ 'dark' if dark else '' }}">

{% if page == 'lock' %}
<div class="card">
    <h2>🔒 Private Valentine</h2>
    <form method="post">
        <input name="password" placeholder="Enter password" required>
        <button class="generate">Unlock 💘</button>
    </form>
</div>

{% elif page == 'generator' %}
<div class="card">
    <h2>💘 Valentine Generator</h2>
    <form action="/proposal">
        <input name="from_name" placeholder="Your name" required>
        <input name="to_name" placeholder="Their name" required>
        <input name="yes_msg" placeholder="Custom YES message" required>
        <input name="password" placeholder="Set a password" required>
        <button class="generate">Generate 💖</button>
    </form>
</div>

{% else %}
<div class="card">
    <button class="darkbtn" onclick="toggle()">🌙 / ☀️</button>
    <h2>{{ from_name }} ❤️ {{ to_name }}</h2>
    <p>Will you be my Valentine?</p>

    <button class="yes" onclick="yes()">YES 💘</button>
    <button class="no" id="no" onclick="move()">NO 🙈</button>

    <button class="share" onclick="share()">Share 💬</button>
</div>

<audio id="music" src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>

<script>
const yesMsg = "{{ yes_msg }}";

function move() {
    const btn = document.getElementById("no");
    btn.style.left = Math.random() * (window.innerWidth - btn.offsetWidth) + "px";
    btn.style.top = Math.random() * (window.innerHeight - btn.offsetHeight) + "px";
}

function yes() {
    document.getElementById("music").play();
    document.body.innerHTML = `
        <div class="card">
            <h2>💖 IT'S A YES 💖</h2>
            <p>${yesMsg}</p>
        </div>
    `;
}

function share() {
    const text = "I just got asked to be a Valentine 💘";
    const url = window.location.href;
    window.open(`https://wa.me/?text=${text} ${url}`);
}

function toggle() {
    document.body.classList.toggle("dark");
}

for (let i = 0; i < 25; i++) {
    let h = document.createElement("div");
    h.className = "heart";
    h.innerHTML = "💖";
    h.style.left = Math.random() * 100 + "vw";
    h.style.animationDelay = Math.random() * 5 + "s";
    document.body.appendChild(h);
}
</script>

{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def lock():
    if request.method == "POST":
        if request.form.get("password") == "love":
            return redirect(url_for("home"))
    return render_template_string(HTML, page="lock")

@app.route("/home")
def home():
    return render_template_string(HTML, page="generator")

@app.route("/proposal")
def proposal():
    return render_template_string(
        HTML,
        page="proposal",
        from_name=request.args.get("from_name"),
        to_name=request.args.get("to_name"),
        yes_msg=request.args.get("yes_msg"),
        dark=False
    )

if __name__ == "__main__":
    app.run()
