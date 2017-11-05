from flask import jsonify
from flask.views import MethodView

from ..app import db


class HealthcheckResource(MethodView):

    def get(self):
        try:
            db.engine.execute("SELECT 1;").fetchone()
            return jsonify({"status": "up"})
        except Exception:
            return jsonify({"status": "down"})
