from flask_restx import Api

from . import tasks

from project.apis.api import vpn_namespace

api = Api(version="2.0", title="Vpn Service Docs", doc="/api/v1/vpn-service/docs")

api.add_namespace(vpn_namespace, path="/api/v1/vpn-service")
