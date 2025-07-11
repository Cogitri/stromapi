import pytz
from simple_dwd_weatherforecast import dwdforecast
from datetime import datetime

from stromapi.config import Config


class Weather:
    __weather: dwdforecast.Weather

    def __init__(self, station_id: str):
        self.__weather = dwdforecast.Weather(station_id)
        self.__weather.update(with_uv=False)

    def __get_forecast(
        self, weatherDataType: dwdforecast.WeatherDataType, timestamp: datetime
    ):
        utc_timestamp = timestamp.astimezone(pytz.utc)
        return self.__weather.get_forecast_data(
            weatherDataType, utc_timestamp, shouldUpdate=False
        )

    @staticmethod
    def __kelvin_to_celcius(k):
        return k - 273.15

    @classmethod
    def from_config(cls, config: Config):
        id = dwdforecast.get_nearest_station_id(config.latitude, config.longitude)
        return cls(id)

    def get_temperature(self, timestamp: datetime) -> str:
        temp = self.__get_forecast(dwdforecast.WeatherDataType.TEMPERATURE, timestamp)
        if temp:
            temp = self.__kelvin_to_celcius(temp)
        return temp

    def get_wind_speed(self, timestamp: datetime) -> str:
        return self.__get_forecast(dwdforecast.WeatherDataType.WIND_SPEED, timestamp)

    def get_wind_gusts(self, timestamp: datetime) -> str:
        return self.__get_forecast(dwdforecast.WeatherDataType.WIND_GUSTS, timestamp)

    def get_wind_direction(self, timestamp: datetime) -> str:
        return self.__get_forecast(
            dwdforecast.WeatherDataType.WIND_DIRECTION, timestamp
        )

    def get_precipitation(self, timestamp: datetime) -> str:
        return self.__get_forecast(dwdforecast.WeatherDataType.PRECIPITATION, timestamp)

    def get_precipitation_probability(self, timestamp: datetime) -> str:
        return self.__get_forecast(
            dwdforecast.WeatherDataType.PRECIPITATION_PROBABILITY, timestamp
        )

    def get_precipitation_duration(self, timestamp: datetime) -> str:
        return self.__get_forecast(
            dwdforecast.WeatherDataType.PRECIPITATION_DURATION, timestamp
        )

    def get_cloud_coverage(self, timestamp: datetime) -> str:
        return self.__get_forecast(
            dwdforecast.WeatherDataType.CLOUD_COVERAGE, timestamp
        )

    def get_sun_duration(self, timestamp: datetime) -> str:
        return self.__get_forecast(dwdforecast.WeatherDataType.SUN_DURATION, timestamp)

    def get_sun_irradiance(self, timestamp: datetime) -> str:
        return self.__get_forecast(
            dwdforecast.WeatherDataType.SUN_IRRADIANCE, timestamp
        )
