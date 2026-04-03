from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api')
def api():
    return jsonify([
        {"name": "item1"},
        {"name": "item2"}
    ])

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    return f"Received {itemName} - {itemDescription}"

if __name__ == '__main__':
    app.run(debug=True)