import csv
import datetime
from typing import List, Tuple
from pathlib import Path

import pytz
import requests

from stromapi.data_cell import DataCell
from stromapi.exceptions.api_error import ApiError
from stromapi.price import Price
from stromapi.weather import Weather


class Collector:
    __weather: Weather
    __token: str
    __base_path: str = "https://ds.netztransparenz.de"

    def __init__(self, token: str):
        self.__token = token

    def run(self, weather: Weather) -> List[DataCell]:
        prices = self.get_spotmarktpreise()
        return [DataCell.from_price(weather, x) for x in prices]

    @staticmethod
    def __get_date_str(delta: int) -> str:
        time = datetime.datetime.now(pytz.utc)
        day = time + datetime.timedelta(days=delta)
        return day.strftime("%Y-%m-%dT%H:%M:%S")

    def get_spotmarktpreise(self) -> List[Price]:
        dateFrom = self.__get_date_str(-1)
        dateTo = self.__get_date_str(1)
        print(f"{self.__base_path}/api/v1/data/Spotmarktpreise/{dateFrom}/{dateTo}")
        resp = requests.get(
            f"{self.__base_path}/api/v1/data/Spotmarktpreise/{dateFrom}/{dateTo}",
            headers=self.__headers(),
        )
        if not resp.ok:
            raise ApiError(resp)

        reader = csv.DictReader(
            resp.text.splitlines(),
            delimiter=";",
            fieldnames=["date", "start", "startTZ", "end", "endTZ", "price"],
        )
        # Skip the header
        reader.__next__()

        result = []
        for row in reader:
            result.append(
                Price.from_api_data(
                    row["date"],
                    row["start"],
                    row["startTZ"],
                    row["end"],
                    row["endTZ"],
                    row["price"],
                )
            )

        return result

    def dump_csv(self, output_path: Path, data_cells: List[DataCell]):
        with open(output_path, "w") as f:
            writer = csv.writer(
                f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(DataCell.csv_header())
            for cell in data_cells:
                writer.writerow(cell.to_csv_row())

    def __headers(self) -> str:
        return {"Authorization": "Bearer {}".format(self.__token)}
