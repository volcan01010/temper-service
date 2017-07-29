from flask_restful import Resource

from temper_app import app
from temper_app.services.temper_service import (
    get_temperature,
    TemperSubProcessError)


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

        try:
            temperature = get_temperature()
            return {"Temperature (Celcius)": "{}".format(temperature)}, 200
        except TemperSubProcessError as e:
            msg = "{}".format(e.args)
            app.logger.debug(msg)
            return {"Error": msg}, 500
        finally:
            app.logger.debug("Request complete")


