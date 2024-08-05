from flask import Flask, render_template_string

app = Flask(__name__)

# CSS
style_css = """
body {
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 50px;
}
"""

# HTML Template
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ad Crest</title>
    <style>{{ style_css }}</style>
</head>
<body>
    <h1>Welcome to Ad Crest!</h1>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_html, style_css=style_css)

if __name__ == '__main__':
    app.run(debug=True)
