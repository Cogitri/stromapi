import tomli


class Config:
    __client_secret: str
    __resolution_in_minutes: int
    __latitude: float
    __longitude: float

    def __init__(self):
        with open("config.toml", "rb") as f:
            toml_dict = tomli.load(f)
        self.__client_secret = toml_dict["entsoe"]["client_secret"]
        self.__resolution_in_minutes = toml_dict["entsoe"]["resolution_in_minutes"]
        self.__latitude = toml_dict["weather"]["latitude"]
        self.__longitude = toml_dict["weather"]["longitude"]

    @property
    def client_secret(self) -> str:
        return self.__client_secret

    @property
    def resolution_in_minutes(self) -> int:
        return self.__resolution_in_minutes

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude
