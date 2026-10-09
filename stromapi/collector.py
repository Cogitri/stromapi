import csv
import datetime
from pathlib import Path

import pytz

from stromapi.data_cell import DataCell
from stromapi.day_ahead_prices import DayAheadPrices
from stromapi.weather import Weather


class Collector:
    __weather: Weather

    def __init__(self):
        pass

    def run(self, day_ahead_prices: DayAheadPrices, weather: Weather) -> list[DataCell]:
        prices = day_ahead_prices.query_day_ahead_prices(
            self.__get_date(-1), self.__get_date(1)
        )
        return [DataCell.from_price(weather, x) for x in prices]

    @staticmethod
    def __get_date(delta: int) -> str:
        time = datetime.datetime.now(pytz.utc)
        day = time + datetime.timedelta(days=delta)
        return day

    def dump_csv(self, output_path: Path, data_cells: list[DataCell]):
        with open(output_path, "w") as f:
            writer = csv.writer(
                f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(DataCell.csv_header())
            for cell in data_cells:
                writer.writerow(cell.to_csv_row())
