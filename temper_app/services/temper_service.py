import subprocess

from temper_app import app


def get_temperature():
    """
    Return the temperature recorded at the chosen sensor
    :return: float, temperature in degrees Celcius
    """
    # Increment call count
    msg = "get_temperature called"
    app.logger.debug(msg)

    # Get the temperature
    try:
        temperature = subprocess.check_output(
            ['/usr/local/bin/temper-poll', '-c', '-s', '1'])
    except FileNotFoundError as e:
        msg = "temper-poll script not found: {}".format(e.strerror)
        app.logger.debug(msg)
        raise TemperSubProcessError(msg)

    try:
        temperature = float(temperature)
    except ValueError:
        msg = "No valid temperature returned.  Check sensor is connected."
        app.logger.debug(msg)
        raise TemperSubProcessError(msg)

    return temperature


class TemperSubProcessError(BaseException):
    """
    Raised if there is a problem with the subprocess command.
    """
    pass
