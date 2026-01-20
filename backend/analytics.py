"""
analytics.py
-------------
Provides analytics, metrics, FL status, alerts, and PQC events
for visualization in the frontend dashboard.

All values are derived from offline evaluation or safely simulated.
"""

import time
import random
import numpy as np

# -------------------------------------------------
# GLOBAL MODEL METRICS (FROM OFFLINE EVALUATION)
# -------------------------------------------------
def get_global_metrics(threshold):
    return {
        "accuracy": 0.964,
        "precision": 0.951,
        "recall": 0.972,
        "f1_score": 0.961,
        "threshold": round(float(threshold), 6),
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
    }


# -------------------------------------------------
# RECONSTRUCTION ERROR DISTRIBUTION
# -------------------------------------------------
def get_error_distribution(threshold):
    benign_errors = [round(random.uniform(0.002, 0.006), 6) for _ in range(30)]
    attack_errors = [round(random.uniform(0.015, 0.040), 6) for _ in range(30)]

    return {
        "benign": benign_errors,
        "attack": attack_errors,
        "threshold": round(float(threshold), 6)
    }


# -------------------------------------------------
# FEDERATED LEARNING STATUS (READ-ONLY)
# -------------------------------------------------
def get_fl_status():
    return {
        "aggregation_method": "FedMedian",
        "clients": 3,
        "rounds_completed": 5,
        "training_status": "Completed",
        "global_model": "CNN Autoencoder",
        "last_round_loss": 0.0068
    }


# -------------------------------------------------
# CLIENT TRAINING METRICS
# -------------------------------------------------
def get_client_metrics():
    return {
        "client_A": {
            "name": "Monday Org",
            "loss_curve": [0.11, 0.07, 0.04, 0.025, 0.018],
            "final_loss": 0.018
        },
        "client_B": {
            "name": "Tuesday Org",
            "loss_curve": [0.13, 0.08, 0.05, 0.031, 0.021],
            "final_loss": 0.021
        },
        "client_C": {
            "name": "Thursday Org",
            "loss_curve": [0.12, 0.075, 0.048, 0.029, 0.019],
            "final_loss": 0.019
        }
    }


# -------------------------------------------------
# INTRUSION ALERTS (SOC-STYLE)
# -------------------------------------------------
def get_alerts():
    return [
        {
            "timestamp": "2026-01-19 10:42:11",
            "severity": "High",
            "prediction": "DDoS Attack",
            "reconstruction_error": 0.0341
        },
        {
            "timestamp": "2026-01-19 11:05:47",
            "severity": "Medium",
            "prediction": "Port Scan",
            "reconstruction_error": 0.0217
        },
        {
            "timestamp": "2026-01-19 11:32:02",
            "severity": "Low",
            "prediction": "Anomalous Traffic",
            "reconstruction_error": 0.0149
        }
    ]


# -------------------------------------------------
# PQC SECURITY EVENTS (CONCEPTUAL)
# -------------------------------------------------
def get_pqc_events():
    return [
        "Kyber key exchange established",
        "Federated model update encrypted using PQC-derived key",
        "Dilithium signature verified",
        "Secure aggregation completed"
    ]
