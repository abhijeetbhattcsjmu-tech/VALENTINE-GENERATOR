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
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.card {
    background: white;
    width: 90%;
    max-width: 400px;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    text-align: center;
    animation: pop 0.5s ease;
}

@keyframes pop {
    from { transform: scale(0.8); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

h1 {
    color: #ff3366;
    margin-bottom: 10px;
}

input {
    width: 100%;
    padding: 15px;
    margin: 12px 0;
    font-size: 16px;
    border-radius: 14px;
    border: 1px solid #ddd;
}

button {
    width: 100%;
    padding: 18px;
    font-size: 18px;
    border-radius: 16px;
    border: none;
    margin-top: 12px;
    cursor: pointer;
}

.generate {
    background:
