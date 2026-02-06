from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Valentine 💘</title>

<style>
* {
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
}

body {
    margin: 0;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card {
    background: white;
    width: 90%;
    max-width: 400px;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    text-align: center;
}

h1 {
    color: #ff4d6d;
    margin-bottom: 10px;
}

input {
    width: 100%;
    padding: 14px;
    margin: 10px 0;
    font-size: 16px;
    border-radius: 12px;
    border: 1px solid #ddd;
}

button {
    width: 100%;
    padding: 16px;
    font-size: 18px;
    border-radius: 14px;
    border: none;
    margin-top: 10px;
    cursor: pointer;
}

.generate {
    background: #ff4d6d;
    color: white;
}

.yes {
    background: #38b000;
    color: white;
}

.no {
    background: #adb5bd;
    color: white;
    position: relative;
}
</style>
</head>

<body>

{% if page == 'generator' %}
<div class="card">
    <h1>💘 Valentine Generator</h1>
    <form action="/proposal">
        <input name="from_name" placeholder="Your name" required>
        <input name="to_name" placeholder="Their name" required>
        <button class="generate">Generate 💖</button>
    </form>
</div>

{% else %}
<div class="card">
    <h1>{{ from_name }} ❤️ {{ to_name }}</h1>
    <p style="font-size:18px;">Will you be my Valentine?</p>

    <button class="yes" onclick="yes()">YES 💘</button>
    <button class="no" id="no" onclick="move()">NO 🙈</button>
</div>

<script>
function move() {
    const btn = document.getElementById("no");
    btn.style.position = "absolute";
    btn.style.left = Math.random() * (window.innerWidth - btn.offsetWidth) + "px";
    btn.style.top = Math.random() * (window.innerHeight - btn.offsetHeight) + "px";
}

function yes() {
    document.body.innerHTML = `
        <div class="card">
            <h1>💖 She Said YES! 💖</h1>
            <p>You are officially a Valentine champion 😎</p>
        </div>
    `;
}
</script>
{% endif %}

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, page="generator")

@app.route("/proposal")
def proposal():
    return render_template_string(
        HTML,
        page="proposal",
        from_name=request.args.get("from_name"),
        to_name=request.args.get("to_name")
    )

if __name__ == "__main__":
    app.run()
