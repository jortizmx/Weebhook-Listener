from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("Received webhook:", data)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("Webhook listener running on http://localhost:5000/webhook")
    app.run(port=5000)
