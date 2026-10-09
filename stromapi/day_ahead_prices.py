from datetime import datetime

import pandas as pd
from entsoe import EntsoePandasClient

from stromapi.config import Config
from stromapi.price import Price


class DayAheadPrices:
    __client: EntsoePandasClient

    def __init__(self, client: EntsoePandasClient):
        self.__client = client

    @classmethod
    def from_config(cls, config: Config):
        client = EntsoePandasClient(api_key=config.client_secret)
        return cls(client)

    def query_day_ahead_prices(self, start: datetime, end: datetime) -> list[Price]:
        country_code = "DE_LU"
        series = self.__client.query_day_ahead_prices(
            country_code,
            start=pd.Timestamp(start),
            end=pd.Timestamp(end),
        )

        if len(series) < 2:
            return []

        resolution = (series.index[1] -series.index[0]) / pd.Timedelta(minutes=1)

        prices = []
        for index, price in series.items():
            prices.append(Price.from_api_data(index, resolution, price))
        return prices
