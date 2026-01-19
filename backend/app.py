from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn
import numpy as np

app = Flask(__name__)
CORS(app)

# -------------------------------------------------
# MODEL DEFINITION (SAME AS TRAINING)
# -------------------------------------------------
class GlobalCNN_Autoencoder(nn.Module):
    def __init__(self, input_features):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),

            nn.Conv1d(32, 16, kernel_size=3, padding=1),
            nn.BatchNorm1d(16),
            nn.ReLU(),

            nn.MaxPool1d(2)
        )

        self.decoder = nn.Sequential(
            nn.Upsample(scale_factor=2),

            nn.Conv1d(16, 32, kernel_size=3, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),

            nn.Conv1d(32, 1, kernel_size=3, padding=1)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


# -------------------------------------------------
# LOAD MODEL & THRESHOLD
# -------------------------------------------------
MODEL_PATH = "models/global/global_federated_model.pt"
THRESHOLD_PATH = "models/global/anomaly_threshold.npy"

threshold = float(np.load(THRESHOLD_PATH))

# Input features = CICIDS numeric feature count
INPUT_FEATURES = 78  # safe fixed value for CICIDS2017

model = GlobalCNN_Autoencoder(INPUT_FEATURES)
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# -------------------------------------------------
# ROUTES
# -------------------------------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Backend running"})


@app.route("/detect", methods=["POST"])
def detect():
    """
    Expects JSON:
    {
        "features": [f1, f2, ..., fN]
    }
    """
    data = request.json.get("features")

    if data is None:
        return jsonify({"error": "No features provided"}), 400

    x = torch.tensor(data, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

    with torch.no_grad():
        recon = model(x)
        error = torch.mean((x - recon) ** 2).item()

    result = "Attack" if error > threshold else "Benign"

    return jsonify({
        "reconstruction_error": error,
        "threshold": threshold,
        "prediction": result
    })


@app.route("/pqc", methods=["GET"])
def pqc_demo():
    return jsonify({
        "kyber": "Post-quantum key exchange simulated",
        "encryption": "Model update encrypted (simulated)",
        "signature": "Dilithium signature verified (simulated)"
    })


# -------------------------------------------------
# RUN
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
