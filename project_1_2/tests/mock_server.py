from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# Mock data for the Kaggle dataset
mock_dataset = {
    "id": "carlmcbrideellis/data-anscombes-quartet",
    "title": "Anscombe's Quartet Dataset",
    "url": "https://www.kaggle.com/carlmcbrideellis/data-anscombes-quartet",
    # Add other relevant information
}

# Mock response for dataset download
mock_download_response = b"Mock dataset content in ZIP archive."

# Endpoint to simulate Kaggle dataset information
@app.route("/datasets/<dataset_id>")
def get_dataset_info(dataset_id):
    if dataset_id == mock_dataset["id"]:
        return jsonify(mock_dataset)
    else:
        return jsonify({"error": "Dataset not found"}), 404

# Endpoint to simulate dataset download
@app.route("/datasets/<dataset_id>/download")
def download_dataset(dataset_id):
    if dataset_id == mock_dataset["id"]:
        # Simulate some processing time
        time.sleep(1)
        return mock_download_response
    else:
        return jsonify({"error": "Dataset not found"}), 404

# Run the Flask app in a separate thread
def run_mock_server():
    app.run(host="127.0.0.1", port=8080)

# Start the Flask app in a separate thread when this script is executed
if __name__ == "__main__":
    server_thread = threading.Thread(target=run_mock_server)
    server_thread.start()
