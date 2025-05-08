from flask import Flask
from prometheus_client import start_http_server, Summary, Counter
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_app_requests_total', 'Total number of requests')

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello, Prometheus!"

if __name__ == "__main__":
    start_http_server(8000)  # Prometheus metrics exposed here
    app.run(host="0.0.0.0", port=5000)
