from flask_restful import Resource


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
        return {"hello": "Temper API"}, 200

