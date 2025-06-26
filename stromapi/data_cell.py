from datetime import datetime

from stromapi.price import Price
from stromapi.weather import Weather


class DataCell:
    __start: datetime
    __end: datetime
    __price: float
    __temperature: str
    __wind_speed: str
    __wind_gusts: str
    __wind_direction: str
    __precipitation: str
    __precipitation_probability: str
    __precipitation_duration: str
    __cloud_coverage: str
    __sun_duration: str
    __sun_irradiance: str

    def __init__(
        self,
        start: datetime,
        end: datetime,
        price: float,
        temperature: str,
        wind_speed: str,
        wind_gusts: str,
        wind_direction: str,
        precipitation: str,
        precipitation_probability: str,
        precipitation_duration: str,
        cloud_coverage: str,
        sun_duration: str,
        sun_irradiance: str,
    ):
        self.__start = start
        self.__end = end
        self.__price = price
        self.__temperature = temperature
        self.__wind_speed = wind_speed
        self.__wind_gusts = wind_gusts
        self.__wind_direction = wind_direction
        self.__precipitation = precipitation
        self.__precipitation_probability = precipitation_probability
        self.__precipitation_duration = precipitation_duration
        self.__cloud_coverage = cloud_coverage
        self.__sun_duration = sun_duration
        self.__sun_irradiance = sun_irradiance

    @classmethod
    def from_price(cls, weather: Weather, price: Price):
        return cls(
            price.start,
            price.end,
            price.price,
            weather.get_temperature(price.start),
            weather.get_wind_speed(price.start),
            weather.get_wind_gusts(price.start),
            weather.get_wind_direction(price.start),
            weather.get_precipitation(price.start),
            weather.get_precipitation_probability(price.start),
            weather.get_precipitation_duration(price.start),
            weather.get_cloud_coverage(price.start),
            weather.get_sun_duration(price.start),
            weather.get_sun_duration(price.start),
        )

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def price(self):
        return self.__price

    @property
    def temperature(self):
        return self.__temperature

    @property
    def wind_speed(self):
        return self.__wind_speed

    @property
    def wind_gusts(self):
        return self.__wind_gusts

    @property
    def wind_direction(self):
        return self.__wind_direction

    @property
    def precipitation(self):
        return self.__precipitation

    @property
    def precipitation_probability(self):
        return self.__precipitation_probability

    @property
    def precipitation_duration(self):
        return self.__precipitation_duration

    @property
    def cloud_coverage(self):
        return self.__cloud_coverage

    @property
    def sun_duration(self):
        return self.__sun_duration

    @property
    def sun_irradiance(self):
        return self.__sun_irradiance

    @staticmethod
    def csv_header():
        return [
            "Zeit Start",
            "Zeit Ende",
            "Preis kw/h (Cent)",
            "Temperatur (Celcius)",
            "Windgeschwindigkeit (m/s)",
            "Windböen (m/s)",
            "Windrichtung (Grad)",
            "Regenmenge (kg/m^2)",
            "Regenwahrscheinlichkeit (Prozent)",
            "Regendauer (Sekunden)",
            "Wolkenbedeckung (Prozent)",
            "Sonnenlänge (Sekunden)",
            "Sonnenstärke (kJ/m^2)",
        ]

    def to_csv_row(self):
        return [
            self.start.strftime("%Y-%m-%d %H:%M:%S"),
            self.end.strftime("%Y-%m-%d %H:%M:%S"),
            self.price,
            self.temperature,
            self.wind_speed,
            self.wind_gusts,
            self.wind_direction,
            self.precipitation,
            self.precipitation_probability,
            self.precipitation_duration,
            self.cloud_coverage,
            self.sun_duration,
            self.sun_irradiance,
        ]
