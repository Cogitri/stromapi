import datetime


class Price:
    __start: datetime.datetime
    __end: datetime.datetime
    __price: float

    def __init__(self, start: datetime.datetime, end: datetime.datetime, price: float):
        self.__start = start
        self.__end = end
        self.__price = price

    @classmethod
    def from_api_data(
        cls,
        start: datetime.datetime,
        intervalMinutes: int,
        priceMwh: float,
    ):
        end = start + datetime.timedelta(minutes=intervalMinutes)
        priceKwh = priceMwh / 10

        return cls(start, end, priceKwh)

    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end

    @property
    def price(self) -> float:
        return self.__price
