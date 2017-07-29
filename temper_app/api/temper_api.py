from flask_restful import Resource

from temper_app import app


class TemperAPI(Resource):

    def get(self):
        """
        Greetings from TemperAPI
        ---
        tags:
          - hello
        produces:
          - application/json
        responses:
            200:
                description: Says hello
            500:
                description: Internal Server Error
        """
        app.logger.debug("Temper endpoint hit")
        return {"hello": "Temper API"}, 200

