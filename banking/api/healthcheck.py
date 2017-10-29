from flask.views import MethodView

from ..app import db


class HealthcheckResource(MethodView):

    def get(self):
        result = db.engine.execute("SELECT 1;").fetchone()
        return "DB: OK {}".format(result)
