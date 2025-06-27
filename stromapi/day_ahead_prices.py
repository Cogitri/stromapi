from datetime import datetime
from typing import List

import pandas as pd
from entsoe import EntsoePandasClient

from stromapi.config import Config
from stromapi.price import Price


class DayAheadPrices:
    __client: EntsoePandasClient
    __resolution: int

    def __init__(self, client: EntsoePandasClient, resolution: int):
        self.__client = client
        self.__resolution = resolution

    @classmethod
    def from_config(cls, config: Config):
        client = EntsoePandasClient(api_key=config.client_secret)
        return cls(client, config.resolution_in_minutes)

    def query_day_ahead_prices(self, start: datetime, end: datetime) -> List[Price]:
        country_code = "DE_LU"
        series = self.__client.query_day_ahead_prices(
            country_code,
            start=pd.Timestamp(start),
            end=pd.Timestamp(end),
            resolution=f"{self.__resolution}min",
        )

        prices = []
        for index, price in series.items():
            prices.append(Price.from_api_data(index, self.__resolution, price))
        return prices
