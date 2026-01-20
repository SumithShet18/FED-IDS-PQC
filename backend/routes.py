"""
routes.py
---------
Defines all analytics and visualization API routes.
Keeps app.py minimal and clean.
"""

from flask import Blueprint, jsonify
from analytics import (
    get_global_metrics,
    get_error_distribution,
    get_fl_status,
    get_client_metrics,
    get_alerts,
    get_pqc_events
)

analytics_bp = Blueprint("analytics_bp", __name__)

# -------------------------------------------------
# GLOBAL MODEL METRICS
# -------------------------------------------------
@analytics_bp.route("/api/global/metrics", methods=["GET"])
def global_metrics():
    from app import threshold
    return jsonify(get_global_metrics(threshold))


# -------------------------------------------------
# RECONSTRUCTION ERROR DISTRIBUTION (FOR GRAPHS)
# -------------------------------------------------
@analytics_bp.route("/api/global/errors", methods=["GET"])
def error_distribution():
    from app import threshold
    return jsonify(get_error_distribution(threshold))


# -------------------------------------------------
# FEDERATED LEARNING STATUS
# -------------------------------------------------
@analytics_bp.route("/api/fl/status", methods=["GET"])
def fl_status():
    return jsonify(get_fl_status())


# -------------------------------------------------
# CLIENT TRAINING METRICS
# -------------------------------------------------
@analytics_bp.route("/api/client/metrics", methods=["GET"])
def client_metrics():
    return jsonify(get_client_metrics())


# -------------------------------------------------
# SOC ALERTS & LOGS
# -------------------------------------------------
@analytics_bp.route("/api/alerts", methods=["GET"])
def alerts():
    return jsonify(get_alerts())


# -------------------------------------------------
# PQC SECURITY EVENTS
# -------------------------------------------------
@analytics_bp.route("/api/security/events", methods=["GET"])
def pqc_events():
    return jsonify(get_pqc_events())
