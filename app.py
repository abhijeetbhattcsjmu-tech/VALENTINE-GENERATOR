from flask import Flask, request, render_template_string
import urllib.parse

app = Flask(__name__)

TEMPLATE = r"""
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
    font-family: Arial, sans-serif;
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
}
input, button {
    width: 100%;
    padding: 14px;
    margin-top: 10px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
}
button { cursor: pointer; }
.yes { background: #2ec4b6; color: white; }
.no { background: #adb5bd; color: white; }
</style>
</head>

<body>

{% if page == "ask" %}
<div class="card">
    <h2>💌 Valentine Time</h2>
    <form>
        <input name="from_name" placeholder="Your Name" required>
        <input name="to_name" placeholder="Your Love's Name" required>
        <button>Continue 💖</button>
    </form>
</div>

{% elif page == "proposal" %}
<div class="card">
    <h2>{{ from_name }} ❤️ {{ to_name }}</h2>
    <p>Will you be my Valentine?</p>

    <button class="yes" onclick="yes()">YES 💘</button>
    <button class="no" onclick="nope()">NO 😅</button>
</div>

<script>
function yes() {
    document.body.innerHTML = `
        <div class="card">
            <h2>💖 YES 💖</h2>
            <p>{{ quote }}</p>
        </div>
    `;
}
function nope() {
    document.body.innerHTML = `
        <div class="card">
            <h2>😅 Oops</h2>
            <p>Better luck next time 💔</p>
        </div>
    `;
}
</script>
{% endif %}

</body>
</html>
"""

@app.route("/")
def generator():
    return """
    <h3>Create Valentine Link</h3>
    <form action="/create">
        <input name="quote" placeholder="YES quote (optional)">
        <input name="password" placeholder="Password (optional)">
        <button>Create Link</button>
    </form>
    """

@app.route("/create")
def create():
    quote = request.args.get("quote") or "You just made this Valentine unforgettable 💖"
    password = request.args.get("password", "")
    data = urllib.parse.quote(f"{quote}|{password}")
    return f"Your link:<br><a href='/v?d={data}'>Open Valentine</a>"

@app.route("/v")
def valentine():
    data = urllib.parse.unquote(request.args.get("d", ""))
    quote, password = data.split("|")

    if password and request.args.get("pass_try") != password:
        return """
        <h3>🔒 Enter Password</h3>
        <form>
            <input name="pass_try" placeholder="Password">
            <button>Unlock</button>
        </form>
        """

    if "from_name" not in request.args:
        return render_template_string(TEMPLATE, page="ask")

    return render_template_string(
        TEMPLATE,
        page="proposal",
        from_name=request.args["from_name"],
        to_name=request.args["to_name"],
        quote=quote
    )

if __name__ == "__main__":
    app.run()
