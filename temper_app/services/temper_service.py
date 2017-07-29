import subprocess

from temper_app import app


def get_temperature(sensor):
    """
    Return the temperature recorded at the chosen sensor
    :param sensor: Sensor name (can be 'probe' or 'sensor')
    :return: float, temperature in degrees Celcius
    """
    # Increment call count
    msg = "get_temperature called with {}".format(sensor)
    app.logger.debug(msg)

    # Check sensor name
    try:
        assert sensor in ('probe', 'sensor')
    except AssertionError:
        msg = "Bad sensor name: must be 'probe' or 'sensor"
        app.logger.debug(msg)
        raise TemperBadSensorNameError(msg)

    sensor_numbers = {'sensor': '0',
                      'probe': '1'}

    # Get the temperature
    try:
        temperature = subprocess.check_output(
            ['/usr/local/bin/temper-poll', '-c', '-s', sensor_numbers[sensor]])
    except subprocess.SubprocessError as e:
        msg = str(e.args)
        app.logger.debug(msg)
        raise TemperBadSensorNameError(msg)

    return temperature


class TemperBadSensorNameError(BaseException):
    """
    Raised when bad temperature sensor name is passed.
    """
    pass


class TemperSubProcessError(BaseException):
    """
    Raised if there is a problem with the subprocess command.
    """
    pass
