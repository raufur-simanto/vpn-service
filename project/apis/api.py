from flask import current_app as app
from flask import request
from flask_restx import Namespace, Resource

vpn_namespace = Namespace("vpn")


class Alive(Resource):
    @vpn_namespace.response(200, "Alive.")
    def get(self):
        response = {}
        response["status"] = "success"
        response["message"] = "Alive."
        return response, 200


vpn_namespace.add_resource(Alive, "/alive")
