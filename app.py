from flask import Flask, request, render_template_string
import urllib.parse

app = Flask(__name__)

HTML = """
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
button {
    cursor: pointer;
}
.yes { background: #2ec4b6; color: white; }
.no { background: #adb5bd; color: white; }
</style>
</head>

<body>

{% if page == "password" %}
<div class="card">
    <h2>🔒 Enter Password</h2>
    <form method="get">
        <input name="pass_try" placeholder="Password" required>
        <button>Unlock 💘</button>
    </form>
</div>

{% elif page == "ask" %}
<div class="card">
    <h2>💌 Valentine Time</h2>
    <form>
        <input name="from_name" placeholder="Your Name" required>
        <input name="to_name" placeholder="Your Love's Name" required>
        <button>Continue 💖</button>
    </form>
</div>

{% elif p
