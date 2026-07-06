# Webhook Listener (Python + Flask)

This simple webhook listener receives POST requests and prints
the JSON payload. Useful for testing integrations and callbacks.

## How to run
pip install flask
python listener.py

## Test with Postman or curl:
curl -X POST http://localhost:5000/webhook -H "Content-Type: application/json" -d '{"event":"test"}'
