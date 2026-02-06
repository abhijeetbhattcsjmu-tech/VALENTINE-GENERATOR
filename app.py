from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Valentine Generator</title>
    <style>
        body { font-family: Arial; text-align: center; background: #ffe6ea; }
        .box { margin-top: 60px; }
        button { padding: 15px 30px; font-size: 18px; margin: 10px; }
    </style>
</head>
<body>
    {% if page == 'generator' %}
        <div class="box">
            <h1>💘 Valentine Generator 💘</h1>
            <form method="get" action="/proposal">
                <input name="from_name" placeholder="Your Name" required><br><br>
                <input name="to_name" placeholder="Crush Name" required><br><br>
                <button type="submit">Generate</button>
            </form>
        </div>
    {% else %}
        <div class="box">
            <h1>{{ from_name }} ❤️ {{ to_name }}</h1>
            <h2>Will you be my Valentine?</h2>
            <button onclick="yes()">YES</button>
            <button id="no" onclick="move()">NO</button>
        </div>
        <script>
            function move() {
                const btn = document.getElementById("no");
                btn.style.position = "absolute";
                btn.style.left = Math.random() * window.innerWidth + "px";
                btn.style.top = Math.random() * window.innerHeight + "px";
            }
            function yes() {
                alert("💖 Yay! Love accepted 💖");
            }
        </script>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, page="generator")

@app.route("/proposal")
def proposal():
    return render_template_string(
        TEMPLATE,
        page="proposal",
        from_name=request.args.get("from_name"),
        to_name=request.args.get("to_name")
    )

if __name__ == "__main__":
    app.run()
