from flask import Flask, request, render_template_string

app = Flask(__name__)

def caesar_cipher(text, shift, mode='e'):
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if mode == 'd':
                new_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Caesar Cipher Tool</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: #f8f9fa;
      color: #212529;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .container {
      max-width: 800px;
      margin-top: 50px;
    }
    .card {
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
      border: none;
    }
    .card-header {
      background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
      color: white;
      font-weight: bold;
      border-radius: 15px 15px 0 0 !important;
    }
    .btn-primary {
      background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
      border: none;
    }
    textarea {
      min-height: 120px;
    }
    .result-box {
      background: #f8f9fa;
      border-radius: 10px;
      padding: 15px;
      border: 1px solid #e9ecef;
      margin-top: 20px;
    }
    .radio-group {
      margin: 15px 0;
    }
    .radio-group label {
      margin-right: 15px;
      font-weight: 500;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="card-header text-center py-3">
        <h2>Caesar Cipher Tool</h2>
      </div>
      <div class="card-body">
        <form method="post" class="mb-4">
          <div class="mb-3">
            <label for="text" class="form-label fw-bold">Enter your text</label>
            <textarea class="form-control" id="text" name="text" required>{{text}}</textarea>
          </div>
          <div class="mb-3">
            <label for="shift" class="form-label fw-bold">Shift Amount</label>
            <input type="number" class="form-control" id="shift" name="shift" value="{{shift}}" required>
          </div>
          <div class="radio-group">
            <label class="form-label fw-bold">Mode:</label>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" id="encrypt" name="mode" value="e" checked>
              <label class="form-check-label" for="encrypt">Encrypt</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" id="decrypt" name="mode" value="d">
              <label class="form-check-label" for="decrypt">Decrypt</label>
            </div>
          </div>
          <button type="submit" class="btn btn-primary w-100 py-2">Process</button>
        </form>
        {% if result %}
        <div class="result-box">
          <h4 class="mb-3">Result</h4>
          <pre style="white-space: pre-wrap;">{{result}}</pre>
        </div>
        {% endif %}
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route("/", methods=['GET', 'POST'])
def index():
    text, shift, mode, result = "", 3, "e", ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form.get('mode', 'e')
        result = caesar_cipher(text, shift, mode)
    return render_template_string(HTML, text=text, shift=shift, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
