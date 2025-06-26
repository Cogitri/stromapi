from datetime import datetime
import pytz


class Price:
    __start: datetime
    __end: datetime
    __price: float

    def __init__(self, start: datetime, end: datetime, price: float):
        self.__start = start
        self.__end = end
        self.__price = price

    @classmethod
    def from_api_data(
        cls, date: str, start: str, startTz: str, end: str, endTz: str, price: str
    ):
        date = datetime.strptime(date, "%d.%m.%Y")
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")

        start = datetime.combine(date, start_time.time())
        end = datetime.combine(date, end_time.time())

        start_tz = pytz.timezone(startTz)
        end_tz = pytz.timezone(endTz)

        start = start_tz.localize(start)
        end = end_tz.localize(end)

        price = float(price.replace(",", "."))

        return cls(start, end, price)

    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end

    @property
    def price(self) -> float:
        return self.__price
